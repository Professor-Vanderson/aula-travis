import pytest
from principal import somar
from principal import subtrair

def test_soma():
    assert somar(2,4)==6

def test_sub():
    assert subtrair(8,3)==5