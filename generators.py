import random
import string

from data import KeyWords
from faker import Faker


class UserData:

# Метод генерации данных для создания нового пользователя
    @staticmethod
    def generate_new_user_data():
        # Метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        # Генерируем email, пароль и имя пользователя
        email = generate_random_string(10) + "@yandex.ru"
        password = generate_random_string(10)
        name = generate_random_string(10)

        # Собираем тело запроса
        user_data = {
        KeyWords.EMAIL: email,
        KeyWords.PASSWORD: password,
        KeyWords.NAME: name
        }
        # Возвращаем словарь с электронной почтой, паролем и именем пользователя
        return user_data


faker = Faker()

def generate_fake_data():
    fake_data = faker.text(max_nb_chars=12)
    return fake_data

def generate_invalid_ingredient_hash():
    fake_hash = faker.random_number(32)
    return f'"{fake_hash}"'
