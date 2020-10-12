# Copyright (C) 2020 by Vd.
# This file is part of EnvReader, the modern environment variables processor.
# EnvReader is released under the MIT License (see LICENSE).


from typing import Callable, Optional

from .field import Field


class FieldGetter(Field):
    def __init__(self, default, alias: str, transform: Callable, description: Optional[str],
                 example: Optional[str], cached: bool):

        super().__init__(default, alias=alias, transform=transform, description=description, example=example)
        self.__cached = cached
        self.__value = None

    def get_value(self):
        if self.__value:
            return self.__value

        val = super().get_value()

        if self.__cached:
            self.__value = val

        return val

    def __get__(self, obj, cls=None):
        return self.get_value()

    def __set__(self, obj, value):
        raise AttributeError("You can't change an env variable from here! Use os.environ for this.")
