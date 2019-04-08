import pytest

from .app import hello


def test_hello():
    assert not hello()
