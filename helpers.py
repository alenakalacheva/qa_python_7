import random
import string
import requests
from endpoints import Endpoints
from faker import Faker

fake = Faker(locale="ru_RU")


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def create_new_courier_data():
    courier = {"login": generate_random_string(7),
               "password": generate_random_string(7),
               "firstName": generate_random_string(7)
               }
    return courier


def create_new_courier():
    payload = create_new_courier_data()
    response = requests.post(Endpoints.COURIER, data=payload)
    if response.status_code == 201:
        return payload


def create_random_order():
    payload = {"firstName": fake.first_name(),
               "lastName": fake.last_name(),
               "address": fake.address(),
               "metroStation": random.randint(1, 215),
               "phone": fake.msisdn(),
               "rentTime": random.randint(1, 7),
               "deliveryDate": fake.date_between(start_date='today', end_date='+1y').strftime("%Y-%m-%d"),
               "comment": fake.text(max_nb_chars=30),
               "color": []
               }
    return payload
