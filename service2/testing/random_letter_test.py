import string
import random
import pytest
from application import routes
from application.routes import random_letter


def test_randletter():
    assert random_letter == 'A' or 'B' or 'C'
