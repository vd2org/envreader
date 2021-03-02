# Copyright (C) 2020 by Vd.
# This file is part of EnvReader, the modern environment variables processor.
# EnvReader is released under the MIT License (see LICENSE).


import os

from envreader import EnvReader


def test_json():
    os.environ['VAR_DICT'] = '{"a": "text", "b": 1, "c": 2.5}'
    os.environ['VAR_LIST'] = '[1, 2, 3, 4, "text"]'
    os.environ['VAR_TUPLE'] = '[9, 8, 7, 6, "text"]'

    class MyEnv(EnvReader):
        VAR_DICT: dict
        VAR_LIST: list
        VAR_TUPLE: tuple

    e = MyEnv()

    assert e.VAR_DICT == {"a": "text", "b": 1, "c": 2.5}
    assert e.VAR_LIST == [1, 2, 3, 4, "text"]
    assert e.VAR_TUPLE == (9, 8, 7, 6, "text")
