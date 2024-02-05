# Copyright (C) 2020-2024 by Vd.
# This file is part of EnvReader, the modern environment variables processor.
# EnvReader is released under the MIT License (see LICENSE).
from __future__ import annotations

import os

from envreader import EnvReader


def test_simple():
    os.environ['VAR_STR'] = "some_string"
    os.environ['VAR_INT'] = "123456"
    os.environ['VAR_FLOAT'] = "123.456"
    os.environ['VAR_BOOL_OK'] = "ok"
    os.environ['VAR_BOOL_TRUE'] = "True"
    os.environ['VAR_BOOL_ON'] = "on"
    os.environ['VAR_BOOL_1'] = "1"
    os.environ['VAR_BOOL_FALSE'] = "False"

    class MyEnv(EnvReader):
        VAR_STR: str
        VAR_INT: int
        VAR_FLOAT: float
        VAR_BOOL_OK: bool
        VAR_BOOL_TRUE: bool
        VAR_BOOL_ON: bool
        VAR_BOOL_1: bool
        VAR_BOOL_FALSE: bool

    e = MyEnv()

    assert e.VAR_STR == "some_string"
    assert e.VAR_INT == 123456
    assert e.VAR_FLOAT == 123.456
    assert e.VAR_BOOL_OK == True
    assert e.VAR_BOOL_TRUE == True
    assert e.VAR_BOOL_ON == True
    assert e.VAR_BOOL_1 == True
    assert e.VAR_BOOL_FALSE == False
