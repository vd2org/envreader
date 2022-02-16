# Copyright (C) 2020-2022 by Vd.
# This file is part of EnvReader, the modern environment variables processor.
# EnvReader is released under the MIT License (see LICENSE).


import os

from envreader import EnvReader, Field


def test_fields():
    os.environ['VAR_STR_R'] = "some_string"
    os.environ['VAR_INT_R'] = "1234"

    class MyEnv(EnvReader):
        VAR_STR: str = Field(..., alias="VAR_STR_R", description="description", example="example")
        VAR_INT: int = Field(123, alias="VAR_INT_R", description="int", example="123")

    e = MyEnv()

    assert e.VAR_STR == "some_string"
    assert e.VAR_INT == 1234

    fields = {i.alias: i for i in e.fields()}

    assert fields['VAR_STR_R'].get_value() == "some_string"
    assert fields['VAR_STR_R'].alias == "VAR_STR_R"
    assert fields['VAR_STR_R'].default is ...
    assert fields['VAR_STR_R'].description == "description"
    assert fields['VAR_STR_R'].example == "example"

    assert fields['VAR_STR_R'].help() == "VAR_STR_R\n    description\n    Example: example"

    assert fields['VAR_INT_R'].get_value() == 1234
    assert fields['VAR_INT_R'].alias == "VAR_INT_R"
    assert fields['VAR_INT_R'].default == 123
    assert fields['VAR_INT_R'].description == "int"
    assert fields['VAR_INT_R'].example == "123"

    assert fields['VAR_INT_R'].help() == "VAR_INT_R\n    int\n    Example: 123\n    Default: 123"

    assert e.help() == "VAR_STR_R\n    description\n    Example: example\n\n" \
                       "VAR_INT_R\n    int\n    Example: 123\n    Default: 123"
