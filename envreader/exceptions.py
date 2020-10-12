# Copyright (C) 2020 by Vd.
# This file is part of EnvReader, the modern environment variables processor.
# EnvReader is released under the MIT License (see LICENSE).


class EnvError(ValueError):
    def __init__(self, field: str, msg: str):
        self.__field = field
        super().__init__(msg)

    @property
    def field(self) -> str:
        return self.__field


class EnvMissingError(EnvError):
    pass


class EnvTransformError(EnvError):
    pass
