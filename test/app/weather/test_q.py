import pytest
from flask import current_app
from app import create_app
from test.app.weather.initialization_db import initialization_db


class TestBasicsCase:

    def __init__(self):
        self.app = None
        self.app_context = None
        self.db = None

    def setup_method(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.db = initialization_db()

    def teardown_method(self):
        self.db.session.remove()
        self.db.drop_all()
        self.app_context.pop()

    def test_app_exists(self):
        assert current_app is None

    def test_app_is_testing(self):
        assert current_app.config['testing'] is True


if __name__ == '__main__':
    pytest.main()
