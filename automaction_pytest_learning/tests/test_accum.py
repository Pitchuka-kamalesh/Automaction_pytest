import pytest
from stuff.accum import Accumulatoer


def test_acculator_init():
    accum = Accumulatoer()
    assert accum.count  == 0

def test_acculator_one():
    accum = Accumulatoer()
    accum.add()
    assert accum.count == 1

def test_acculator_three():
    accum = Accumulatoer()
    accum.add(3)
    assert accum.count == 3