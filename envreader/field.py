# Copyright (C) 2020 by Vd.
# This file is part of EnvReader, the modern environment variables processor.
# EnvReader is released under the MIT License (see LICENSE).


import os
from typing import Any, Optional, Callable

from .exceptions import EnvMissingError, EnvTransformError


class Field:
    def __init__(self, default=..., *, alias: Optional[str] = None, transform: Optional[Callable] = None,
                 description: Optional[str] = None, example: Optional[str] = None):
        self.__default = default
        self.__alias = alias
        self.__description = description
        self.__example = example
        self.__transform = transform.__func__ if isinstance(transform, staticmethod) else transform

        if self.__transform and not callable(self.__transform):
            raise TypeError("Unsupported transform value! Use callable class, function, lambda or staticmethod!")

    @property
    def default(self) -> Any:
        return self.__default

    @property
    def alias(self) -> Optional[str]:
        return self.__alias

    @property
    def transform(self) -> Optional[Callable]:
        return self.__transform

    @property
    def description(self) -> Optional[str]:
        return self.__description

    @property
    def example(self) -> Optional[str]:
        return self.__example

    def get_value(self) -> Any:
        val = os.environ.get(self.__alias)

        if val is None and self.__default is ...:
            raise EnvMissingError(self.__alias, f"Required environment variable `{self.__alias}` was not found!")

        if val is None:
            val = self.__transform(self.__default)
            val = self.__default

        try:
            return self.__transform(val)
        except Exception:
            raise EnvTransformError(self.__alias,
                                    f"Cannot transform field `{self.__alias}`! Probably it have wrong format!")

    def help(self) -> str:
        res = self.__alias
        if self.__description:
            res = f"{res}\n    {self.__description}"
        if self.__example or self.__default is not ...:
            res = f"{res}\n    Example: {self.__example or self.__default}"
        if self.__default is not ...:
            res = f"{res}\n    Default: {self.__default}"

        return res
