import pytest
from db import SESSION
from models import User


@pytest.fixture(autouse=True)
def preinit():
    """
    Pytest decorator to run preprcessing proceduce before each test case
    ex: init database and cache
    """
    SESSION.merge(User(**{"uid": "F74094716", "token": "12345"}))
    SESSION.commit()
