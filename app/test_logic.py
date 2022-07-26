import pytest
from logic import PasswordGenerator


def test_answer():
    password_length = 8
    p = PasswordGenerator(length=int(password_length))
    password = p.password_generator()

    assert password_length == len(password)
