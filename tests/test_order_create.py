import json
import allure
import pytest
import requests
from endpoints import Endpoints


class TestOrderCreate:
    @pytest.mark.parametrize('color', [['BLACK'], ['GREY'], ['BLACK', 'GREY'], None])
    @allure.title('Проверка заказа с разными вариантами поля цвет')
    def test_order_with_different_colors(self, create_order_data, color):
        payload = create_order_data
        payload["color"] = color
        response = requests.post(Endpoints.ORDER, data=payload)
        assert response.status_code == 201 and "track" in response.text




