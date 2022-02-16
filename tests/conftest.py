import sys

if sys.version_info.major == 3 and sys.version_info.minor < 7:
    collect_ignore = ["test_simple_annotations.py"]
