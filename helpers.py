import requests
import allure
import random
import string
import json
from data import Url, OrderTestData

@allure.step('Регистрируем нового курьера и возвращаем учетные данные')
def register_new_courier_and_return_login_password():
    credentials = {}

    username = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": username,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(Url.BASE_URL + Url.CREATE_COURIER_HANDLE, json=payload)

    if response.status_code == 201:
        credentials = {
            "login": username,
            "password": password,
            "firstName": first_name,
            "status_code": response.status_code,
            "json": response.json()
        }

    return credentials

@allure.step('Генерируем случайную строку')
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

@allure.step('Выполняем вход курьера')
def login_courier(login, password):
    payload = {
        'login': login,
        'password': password
    }
    response = requests.post(Url.BASE_URL + Url.LOGIN_COURIER_HANDLE, json=payload)
    return response

@allure.step('Удаляем курьера по ID')
def delete_courier(courier_id):
    response = requests.delete(f'{Url.BASE_URL}{Url.CREATE_COURIER_HANDLE}/{courier_id}')
    return response

@allure.step('Создаем заказ с цветом')
def create_order(color):
    OrderTestData.ORDER['color'] = color
    payload = OrderTestData.ORDER
    response = requests.post(Url.BASE_URL + Url.ORDERS_HANDLE, data=json.dumps(payload))
    return response

@allure.step('Получаем идентификаторы заказов')
def get_order_ids():
    response = requests.get(Url.BASE_URL + Url.ORDERS_HANDLE)
    response_data = json.loads(response.text)
    order_ids = [order['id'] for order in response_data['orders']]
    return order_ids

