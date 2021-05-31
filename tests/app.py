from api.v1.app import app
import pytest
from flask import Response

@pytest.fixture
def pyte():
    py = app()
    return  py
