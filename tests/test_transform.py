# Copyright (C) 2020-2022 by Vd.
# This file is part of EnvReader, the modern environment variables processor.
# EnvReader is released under the MIT License (see LICENSE).


import os
from typing import Tuple

from envreader import EnvReader, Field


def test_transform():
    os.environ['VAR_LIST_STR'] = "a, b, c, d"
    os.environ['VAR_LIST_INT'] = "1, 2, 3, 4, 5, 6"

    class MyEnv(EnvReader):
        @staticmethod
        def transform_list_int(x: str) -> Tuple[int]:
            return tuple([int(x.strip()) for x in x.split(',')])

        VAR_LIST_STR: Tuple[str] = Field(transform=lambda x: tuple([x.strip() for x in x.split(',')]))
        VAR_LIST_INT: Tuple[int] = Field(transform=transform_list_int)

    e = MyEnv()

    assert e.VAR_LIST_STR == ('a', 'b', 'c', 'd')
    assert e.VAR_LIST_INT == (1, 2, 3, 4, 5, 6)
