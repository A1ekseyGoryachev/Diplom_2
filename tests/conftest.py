import pytest

from generators import UserData
from user_methods import CreateUser, DeleteUser
from helper_methods import HelperMethods
from data import StatusCodes


# Создаем пользователя и сохраняем его данные для удаления после завершения тестов
@pytest.fixture
def generate_user():
    # Генерируем email, пароль и имя нового пользователя
    user_data = UserData.generate_new_user_data()
    # Отправляем запрос на создание уникального пользователя
    response = CreateUser.register_new_user(user_data)
    # Проверяем код статуса полученного ответа при созданиии уникального пользователя (200)
    HelperMethods.check_status_code(response, StatusCodes.OK)
    # Получаем тело ответа в виде словаря
    response_dict = response.json()
    # Получаем авторизационный токен
    access_token = HelperMethods.get_access_token(response_dict)
    # Возвращаем данные пользователя, тело ответа на создание пользователя и авторизационный токен
    yield [user_data, response_dict, access_token]
    # Удаляем созданного пользователя после завершения теста
    DeleteUser.delete_user(access_token)
