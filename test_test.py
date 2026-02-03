from test import add
from app import disp

def test_disp():
    assert disp()

def test_add():
    assert add(2, 3) == 5
