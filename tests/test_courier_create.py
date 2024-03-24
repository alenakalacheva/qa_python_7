import requests
from endpoints import Endpoints
import allure
from data import Data
import pytest


class TestCourierCreate:
    @allure.title('Проверка создания курьера')
    def test_create_courier_success(self, new_courier):
        payload = new_courier
        response = requests.post(Endpoints.COURIER, data=payload)
        assert response.status_code == 201 and response.text == '{"ok":true}'

    @allure.title('Проверка создания курьера без имени')
    def test_create_courier_without_name(self, new_courier):
        payload = new_courier
        del payload["firstName"]
        response = requests.post(Endpoints.COURIER, data=payload)
        assert response.status_code == 201 and response.text == '{"ok":true}'

    @allure.title('Проверка невозможности создать дубль курьера')
    def test_courier_duplicate(self, new_courier):
        payload = new_courier
        requests.post(Endpoints.COURIER, data=payload)
        response = requests.post(Endpoints.COURIER, data=payload)
        assert response.status_code == 409 and response.json()["message"] == Data.ERROR_MESSAGE_1

    @allure.title('Проверка создания курьера без обязательных полей')
    @pytest.mark.parametrize('field', ["login", "password"])
    def test_create_courier_without_required(self, new_courier_no_del, field):
        payload = new_courier_no_del
        del payload[field]
        response = requests.post(Endpoints.COURIER, data=payload)
        assert response.status_code == 400 and response.json()["message"] == Data.ERROR_MESSAGE_2


