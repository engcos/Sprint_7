import allure
import helpers
from data import Messages

@allure.story('Тесты на вход курьера')
class TestCourierLogin:
    @allure.title('Тест успешного входа')
    def test_successful_courier_login(self, courier):
        response = helpers.login_courier(courier['login'], courier['password'])
        assert response.status_code == 200 and 'id' in response.text, \
            f'Status code: {response.status_code}, Response: {response.text}'

    @allure.title('Тест входа с незаполненным полем "login"')
    def test_courier_login_with_empty_login(self, courier):
        response = helpers.login_courier('', courier['password'])
        assert response.status_code == 400 and response.json()['message'] == Messages.LOGIN_BAD_REQUEST_400, \
            f"Status code: {response.status_code}, Response message: {response.json()}"

    @allure.title('Тест входа с незаполненным полем "password"')
    def test_courier_login_with_empty_password(self, courier):
        response = helpers.login_courier(courier['login'], '')
        assert response.status_code == 400 and response.json()['message'] == Messages.LOGIN_BAD_REQUEST_400, \
            f"Status code: {response.status_code}, Response message: {response.json()}"

    @allure.title('Тест входа с неверно заполненным полем "login"')
    def test_courier_login_with_incorrect_login(self, courier):
        response = helpers.login_courier(courier['password'], courier['password'])
        assert response.status_code == 404 and response.json()['message'] == Messages.LOGIN_NOT_FOUND_404, \
            f"Status code: {response.status_code}, Response message: {response.json()}"

    @allure.title('Тест входа с неверно заполненным полем "password"')
    def test_courier_login_with_incorrect_password(self, courier):
        response = helpers.login_courier(courier['login'], courier['login'])
        assert response.status_code == 404 and response.json()['message'] == Messages.LOGIN_NOT_FOUND_404, \
            f"Status code: {response.status_code}, Response message: {response.json()}"
