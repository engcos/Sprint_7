import pytest
import helpers

@pytest.fixture(scope='function')
def courier():
    courier = helpers.register_new_courier_and_return_login_password()
    courier_id = helpers.login_courier(courier['login'], courier['password']).json()['id']
    yield courier
    helpers.delete_courier(courier_id)
