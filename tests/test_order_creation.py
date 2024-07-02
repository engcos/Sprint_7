import allure
import pytest
import helpers
import requests
from data import OrderTestData
from data import Url

@allure.story('Создание заказа')
class TestOrderCreation:
    @allure.title('Тест успешного создания заказа')
    @allure.step('Проверка успешного создания заказа с различными цветами')
    @pytest.mark.parametrize('color', OrderTestData.SCOOTER_COLORS)
    def test_successful_order_creation(self, color):
        response = helpers.create_order(color)
        assert 'track' in response.text, f"Response text: {response.text}"

        @allure.story('Список заказов')
        class TestOrderList:
            @allure.title('Тест успешного получения списка заказа')
            def test_successful_get_order_list(self):
                response = requests.get(Url.BASE_URL + Url.ORDERS_HANDLE)
                assert 'orders' in response.text

