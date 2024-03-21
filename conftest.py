import pytest
import helpers
import requests
from endpoints import Endpoints


@pytest.fixture
def new_courier():
    payload = helpers.create_new_courier_data()
    yield payload
    del payload["firstName"]
    response = requests.post(Endpoints.COURIER_LOGIN, data=payload)
    courier_id = response.json()["id"]
    requests.delete(f'{Endpoints.COURIER}{courier_id}')


@pytest.fixture
def new_courier_no_name():
    payload = helpers.create_new_courier_data()
    yield payload
    response = requests.post(Endpoints.COURIER_LOGIN, data=payload)
    courier_id = response.json()["id"]
    requests.delete(f'{Endpoints.COURIER}{courier_id}')


@pytest.fixture
def new_courier_no_del():
    payload = helpers.create_new_courier_data()
    yield payload


@pytest.fixture
def create_new_courier():
    payload = helpers.create_new_courier()
    yield payload
    response = requests.post(Endpoints.COURIER_LOGIN, data=payload)
    courier_id = response.json()["id"]
    requests.delete(f'{Endpoints.COURIER}{courier_id}')


@pytest.fixture
def create_order_data():
    payload = helpers.create_random_order()
    yield payload


@pytest.fixture
def create_order():
    payload = helpers.create_random_order()
    requests.post(Endpoints.ORDER, data=payload)
    yield
