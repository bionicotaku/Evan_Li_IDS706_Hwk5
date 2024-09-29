import os
import sys
import re
from mylib import add


def os_and_sys_version():
    python_version = re.search(r"\d+\.\d+", sys.version).group()
    os_name = os.getenv("RUNNER_OS")
    return python_version, os_name


def main():
    test_result = add.add(1, 2)
    py_v, os_n = os_and_sys_version()
    print(test_result)
    print(f"Python version: {py_v}, OS: {os_n}")


if __name__ == "__main__":
    main()
