import allure
import requests
from endpoints import Endpoints


class TestOrderList:
    @allure.title('Проверка наличия списка в ответе')
    def test_order_list(self, create_order):
        response = requests.get(Endpoints.ORDER)
        assert response.status_code == 200 and 'orders' in response.json() and len(response.json()['orders']) != 0