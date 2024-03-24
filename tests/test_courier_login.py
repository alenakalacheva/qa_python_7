import allure
import pytest
import requests
from endpoints import Endpoints
from data import Data


class TestCourierLogin:
    @allure.title('Проверка авторизации курьера')
    def test_courier_login(self, create_new_courier):
        payload = create_new_courier
        response = requests.post(Endpoints.COURIER_LOGIN, data=payload)
        assert response.status_code == 200 and "id" in response.text

    @allure.title('Проверка авторизации курьера без обязательных полей')
    @pytest.mark.parametrize('field', ["login", "password"])
    def test_courier_login_without_required(self, create_new_courier, field):
        payload = create_new_courier.copy()

        del payload[field]
        response = requests.post(Endpoints.COURIER_LOGIN, data=payload)
        assert response.status_code == 400 and response.json()["message"] == Data.ERROR_MESSAGE_4

    @allure.title('Проверка авторизации курьера c некорректными данными ')
    @pytest.mark.parametrize('field', ["login", "password"])
    def test_courier_login_wrong_data(self, create_new_courier, field):
        payload = create_new_courier.copy()

        payload[field] += 'wrong'
        response = requests.post(Endpoints.COURIER_LOGIN, data=payload)
        assert response.status_code == 404 and response.json()["message"] == Data.ERROR_MESSAGE_3

