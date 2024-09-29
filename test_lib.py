from mylib import add


def test_add():
    """Function calling add"""
    assert add.add(1, 2) == 3
    assert add.add(3, 4) == 7
    assert add.add(5, 6) == 11
    assert add.add(7, 8) == 15
