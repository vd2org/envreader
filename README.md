# EnvReader

Environment variables parser with types! Yes!

Every time when you make new service you need some class to receive, validate and store environment variables.

With this package it’ll be easy and funny.

Just make a class with typed fields and... that’s it.

### Requirements

Python 3.6 and above. There's no additional dependencies.

### Installation

`pip install envreader`

### Simple usage

```python
from envreader import EnvReader


class MyEnv(EnvReader):
    PATH: str
    LIST: list
    NONE_EXIST: int = 1234  # Variable with default value


e = MyEnv()

print(e.PATH)
# /usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin

print(e.LIST)
# [1, 2, 3, 4]

print(e.NONE_EXIST)
# 1234
```

### Use with transform functions

I don’t want to make a giant validation library like wonderful **Pydantic**. Thus EnvReader supports only simple types(
bool, str, int, float, list, tuple and dict) by default. This is enough in most cases.

Transform functions allows using EnvReader for more complex cases.

```python
from typing import List
from envreader import EnvReader, Field


class MyEnv(EnvReader):
    PATH: List[str] = Field(transform=lambda x: x.split(":"))


e = MyEnv()

print(e.PATH)
# ['/usr/local/bin', '/usr/bin', '/bin', '/usr/sbin', '/sbin']
```

### Using static methods as a transform functions.

You may store all your helper functions inside the same class. But don’t forget to add @staticmethod decorator.

```python
from typing import List
from envreader import EnvReader, Field


class MyEnv(EnvReader):
    @staticmethod
    def trans(x: str) -> List[str]:
        return x.split(':')

    PATH: List[str] = Field(transform=trans)


e = MyEnv()

print(e.PATH)
# ['/usr/local/bin', '/usr/bin', '/bin', '/usr/sbin', '/sbin']
```

### Make your environment variables self-documented.

Documentation is in great demand for all good applications, right?

```python
from envreader import EnvReader, Field


class MyEnv(EnvReader):
    PATH: str = Field("/sbin", description="Application path", example="/usr/bin:/bin:/usr/sbin:/sbin")


e = MyEnv()

print(e.help())
# PATH
#     Application path
#     Example: /usr/bin:/bin:/usr/sbin:/sbin
#     Default: /sbin
```

### Error handling? Easy.

```python
import sys
from envreader import EnvReader, EnvMissingError


class MyEnv(EnvReader):
    SOME_VAR: str


try:
    e = MyEnv()
except EnvMissingError as e:
    print(f"Missing required env var {e.field}")
    sys.exit(-1)
# Missing required env var SOME_VAR
```

#### Enjoy!
