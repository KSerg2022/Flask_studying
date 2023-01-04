import pytest
from flask import current_app


from app import create_app
from app.config import config
from test.app.weather.initialization_db import initialization_db


class TestCaseBasics:

    def setup_method(self):
        self.app = create_app(config_name='testing')
        self.app.test_client()
        self.app.test_cli_runner()
        initialization_db()

    def teardown_method(self):
        self.app.delete()

    def test_start(self):
        response = current_app.test_client().get('/')
        assert response.status_code == 200
        assert response.data.decode('utf-8') == 'Welcome to the web application'

    def test_app_exists(self):
        # print(self.app_context())
        # print(self.app_context)
        print(self.app.config.from_object())
        print(current_app)
        assert current_app is None

    def test_app_is_testing(self):
        q = current_app.config['TESTING']
        print(q)
        assert current_app.config['TESTING'] is True

    def test_body(self):
        assert True is True


# @pytest.fixture()
# def app():
#     app = create_app('testing')
#     app.config.update({
#         'testing': True,
#                        })
#     yield app
#     app.delete()
#
#
# @pytest.fixture()
# def client(app):
#     return app.test_client()
#
#
# @pytest.fixture()
# def runner(app):
#     return app.test_cli_runner()
#
#
# def test_start(client):
#     response = client.get('/')
#     print(response.data)
#     print(response.data.decode('utf-8'))
#     assert response.status_code == 200
#     assert 'Welcome to the web application' in response.data.decode('utf-8')


if __name__ == '__main__':
    pytest.main()


# https://docs-python.ru/packages/veb-frejmvork-flask-python/testirovanie-prilozhenij-flask/