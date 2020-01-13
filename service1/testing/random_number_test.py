import pytest
from application.routes import random_number

def test_randnum():
    assert random_number == '1' or '2' or '3'
