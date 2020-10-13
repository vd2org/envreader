# Copyright (C) 2020 by Vd.
# This file is part of EnvReader, the modern environment variables processor.
# EnvReader is released under the MIT License (see LICENSE).


from typing import Any, List

from .field import Field
from .field_getter import FieldGetter


class EnvReader:
    __transforms = {
        str: lambda x: str(x),
        int: lambda x: int(str(x)),
        float: lambda x: float(str(x)),
        bool: lambda x: str(x).strip().lower() in ('1', 'true', 'ok', 'on', 'yes', 'y')
    }

    def __new__(cls: Any, *args, cached: bool = True, populate: bool = True, **kwargs):
        _attrs = {}

        for attr, attr_type in cls.__annotations__.items():
            _field: Field = getattr(cls, attr, None)

            if not isinstance(_field, Field):
                _field = Field(... if _field is None else _field, alias=attr)

            if attr_type not in cls.__transforms and not _field.transform:
                raise TypeError(f"Unsupported type {attr_type} for field `{attr}`. "
                                f"Supported field types is {list(cls.__transforms.keys())}. "
                                f"Please provide transform function!")

            _field_getter = FieldGetter(
                default=_field.default,
                alias=_field.alias or attr,
                transform=_field.transform or cls.__transforms[attr_type],
                description=_field.description,
                example=_field.example,
                cached=cached
            )

            if populate:
                _field_getter.get_value()

            _attrs[attr] = _field_getter

        return super().__new__(type(cls.__name__, (cls,), _attrs))

    def fields(self) -> List[Field]:
        values = type(self).__dict__.values()
        return [i for i in values if isinstance(i, FieldGetter)]

    def help(self) -> str:
        return "\n\n".join([i.help() for i in self.fields()])
