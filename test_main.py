"""
Test goes here

"""

from main import os_and_sys_version


def test_os_and_sys_version():
    """Function calling os_and_sys_version"""
    python_version, os_name = os_and_sys_version()
    python_version_check = ["3.7", "3.8", "3.9", "3.10", "3.11"]
    os_name_check = ["Windows", "Linux"]
    assert python_version in python_version_check
    # if environment has an OS installed
    if os_name is not None:
        assert os_name in os_name_check


if __name__ == "__main__":
    test_os_and_sys_version()
