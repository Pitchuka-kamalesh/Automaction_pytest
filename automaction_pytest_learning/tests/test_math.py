import pytest


def test_one_plus_one():
    assert 1 + 1 == 2


# def test_one_plus_two(): failed test case to check the report 
#     a = 1
#     b = 2
#     c = 0
#     assert a + b  == c


def test_one_plus_two():
    a = 1
    b = 2
    c = 3
    assert a + b == c


def test_divid_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1/0
    assert "division by zero" in str(e.value)

