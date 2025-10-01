import allure
import pytest

from data import KeyWords, StatusCodes, ResponseMessages as RM
from generators import generate_fake_data
from helper_methods import HelperMethods
from user_methods import LoginUser



class TestLoginUser:

    @allure.title('Проверка возможности входа под существующим пользователем')
    def test_login_an_existing_user(self, generate_user):
        with allure.step('Получаем набор данных зарегистрированного уникального пользователя'):
            user_data = generate_user[0]
        with allure.step('Получаем "email" и "name" зарегистрированного уникального пользователя для авторизации'):
            email = user_data[KeyWords.EMAIL]
            password = user_data[KeyWords.PASSWORD]
        with allure.step('Отправляем запрос на авторизацию пользователя'):
            response = LoginUser.auth_user(email, password)
        with allure.step('Проверяем код статуса ответа при авторизации пользователя - 200'):
            HelperMethods.check_status_code(response, StatusCodes.OK)
        with allure.step('Проверяем, что в теле ответа содержится ключ "success" со значением "True" и присваиваем его переменной'):
            response_value = HelperMethods.is_key_in_response_body(response.json(), KeyWords.SUCCESS)
        with allure.step('Сверяем фактическое значение ключа "success" в теле ответа с ожидаемым - "True"'):
            assert response_value, f'Неверное значение ключа "{KeyWords.SUCCESS}" в теле ответа'


    @allure.title('Проверка возможности входа с неверным логином или паролем')
    @pytest.mark.parametrize('field_name', [
        KeyWords.EMAIL,
        KeyWords.PASSWORD,
    ])
    def test_impossible_to_login_without_login_and_password(self, generate_user, field_name):
        with allure.step('Получаем набор данных созданного уникального пользователя'):
            user_data = generate_user[0]
        with allure.step('Удаляем из набора данных созданного уникального пользователя значение поля "name"'):
            user_data.pop(KeyWords.NAME)
        with allure.step('Присваиваем обязательным полям "email" и "password" неверные значения'):
            user_data[field_name] = generate_fake_data()
        with allure.step('Отправляем запрос на авторизацию пользователя'):
            response = LoginUser.auth_user(user_data[KeyWords.EMAIL], user_data[KeyWords.PASSWORD])
        with allure.step('Проверяем, что код статуса ответа при неуспешной авторизации пользователя - 401'):
            HelperMethods.check_status_code(response, StatusCodes.UNAUTHORIZED)
        with allure.step('Проверяем, что в теле ответа содержится ключ "success" со значением "False" и присваиваем его переменной'):
            response_value = HelperMethods.is_key_in_response_body(response.json(), KeyWords.SUCCESS)
        with allure.step('Сверяем фактическое значение ключа "success" в теле ответа с ожидаемым - "False"'):
            assert not response_value, f'Неверное значение ключа "{KeyWords.SUCCESS}" в теле ответа'
        with allure.step('Проверяем, что в теле ответа содержится ключ "message", получаем его значение и присваиваем его переменной'):
            response_message = HelperMethods.is_key_in_response_body(response.json(), KeyWords.MESSAGE)
        with allure.step('Сравниваем фактическое значение ключа "message" в теле ответа с ожидаемым'):
            assert response_message == RM.INCORRECT_EMAIL_OR_PASSWORD, f'Неверный текст поля {KeyWords.MESSAGE}'
