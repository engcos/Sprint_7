import allure
import helpers
from data import Messages

@allure.story('Тесты удаления курьера')
class TestCourierDeletion:
    @allure.title('Тест успешного удаления курьера')
    @allure.step('Проверка успешного удаления курьера')
    def test_successful_courier_deletion(self, courier):
        courier_id = helpers.login_courier(courier["login"], courier["password"]).json()["id"]
        response = helpers.delete_courier(courier_id)
        assert response.json() == {'ok': True}

    @allure.title('Тест удаления курьера без id')
    @allure.step('Проверка удаления курьера без ID')
    def test_courier_deletion_without_id(self, courier):
        response = helpers.delete_courier('')
        assert response.status_code == 404 and response.json().get('message') == "Not Found.", \
            f'Status code: {response.status_code}, Response message: {response.json().get("message")}'

    @allure.title('Тест удаления курьера с несуществующим id')
    @allure.step('Проверка удаления курьера с несуществующим ID')
    def test_courier_deletion_with_incorrect_id(self, courier):
        response = helpers.delete_courier('1')
        assert response.status_code == 404 and response.json().get('message') == Messages.DELETING_COURIER_404, \
            f'Status code: {response.status_code}, Response message: {response.json().get("message")}'
