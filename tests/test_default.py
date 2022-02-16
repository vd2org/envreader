# Copyright (C) 2020-2022 by Vd.
# This file is part of EnvReader, the modern environment variables processor.
# EnvReader is released under the MIT License (see LICENSE).


import os

from envreader import EnvReader, Field


def test_default():
    os.environ['VAR_EXIST_1'] = "some_string"
    os.environ['VAR_EXIST_2'] = "some_string"

    class MyEnv(EnvReader):
        VAR_STR: str = Field("some_string")
        VAR_INT_1: int = 123456
        VAR_INT_2: int = "123456"
        VAR_EXIST_1: str = "XXXXXX"
        VAR_EXIST_2: str

    e = MyEnv()

    assert e.VAR_STR == "some_string"
    assert e.VAR_INT_1 == 123456
    assert e.VAR_INT_2 == 123456
    assert e.VAR_EXIST_1 == "some_string"
    assert e.VAR_EXIST_2 == "some_string"

    fields = {i.alias: i for i in e.fields()}

    assert fields['VAR_STR'].default == "some_string"
    assert fields['VAR_INT_1'].default == 123456
    assert fields['VAR_INT_2'].default == "123456"
    assert fields['VAR_EXIST_1'].default == "XXXXXX"
    assert fields['VAR_EXIST_2'].default is ...
