import allure
import pytest


from data import KeyWords, StatusCodes, ResponseMessages as RM
from generators import UserData
from helper_methods import HelperMethods
from user_methods import CreateUser, DeleteUser



class TestCreateNewUser:

    @allure.title('Проверяем, что при регистрации уникального пользователя в теле ответа на запрос присутствует ключ "success" со значением "True"')
    def test_create_new_user_successfully(self):
        with allure.step('Генерируем данные уникального пользователя'):
            user_data = UserData.generate_new_user_data()
        with allure.step('Отправляем запрос на создание уникального пользователя'):
            response = CreateUser.register_new_user(user_data)
        with allure.step('Проверяем, что код статуса ответа при созданиии уникального пользователя - 200'):
            HelperMethods.check_status_code(response, StatusCodes.OK)
        with allure.step('Проверяем, что в теле ответа содержится ключ "success" со значением "True" и присваиваем его переменной'):
            response_value = HelperMethods.is_key_in_response_body(response.json(), KeyWords.SUCCESS)
        with allure.step('Получаем авторизационный токен'):
            access_token = HelperMethods.get_access_token(response.json())
        with allure.step('Удаляем созданного пользователя'):
            DeleteUser.delete_user(access_token)
        with allure.step('Сравниваем фактическое значение ключа "success" в теле ответа с ожидаемым - "True"'):
            assert response_value, f'Неверное значение ключа {KeyWords.SUCCESS} в теле ответа'


    @allure.title('Проверяем, что при регистрации уникального пользователя в теле ответа содержатся "email" и "name", отправленные в запросе на регистрацию')
    def test_create_new_user_get_email_and_name(self):
        with allure.step('Генерируем данные уникального пользователя'):
            user_data = UserData.generate_new_user_data()
        with allure.step('Отправляем запрос на создание уникального пользователя'):
            response = CreateUser.register_new_user(user_data)
        with allure.step('Проверяем, что код статуса ответа при созданиии уникального пользователя - 200'):
            HelperMethods.check_status_code(response, StatusCodes.OK)
        with allure.step('Получаем тело ответа в виде словаря'):
            response_body = response.json()
        with allure.step('Проверяем, что в теле ответа содержится ключ "user"'):
            assert KeyWords.USER in response_body, f'В теле ответа отсутствует ключ {KeyWords.USER}'
        with allure.step('Проверяем, что в теле ответа ключ "user" содержится в виде словаря'):
            assert type(HelperMethods.is_key_in_response_body(response_body, KeyWords.USER)) is dict, f'Данные в ответе на запрос в поле {KeyWords.USER} содержатся не в виде словаря'
        with allure.step('Назначаем переменную словарю, полученному по ключу "user"'):
            user_dict = HelperMethods.is_key_in_response_body(response_body, KeyWords.USER)
        with allure.step('Получаем значение ключа "email" из данных, отправленных в запросе на регистрацию уникального пользователя'):
            email = user_data[KeyWords.EMAIL]
        with allure.step('Получаем в теле ответа значение ключа "email" из словаря "user"'):
            email_response = user_dict[KeyWords.EMAIL]
        with allure.step('Проверяем, что "email", отправленный в запросе, и "email", полученный в теле ответа на запрос, совпадают'):
            assert email == email_response, f'"{email}", указанный в запросе, и "{email}", полученный в теле ответа на запрос, НЕ совпадают'
        with allure.step('Получаем значение ключа "name" из данных, отправленных в запросе на регистрацию уникального пользователя'):
            name = user_data[KeyWords.NAME]
        with allure.step('Получаем в теле ответа значение ключа "name" из словаря "user"'):
            name_response = user_dict[KeyWords.NAME]
        with allure.step('Получаем авторизационный токен'):
            access_token = HelperMethods.get_access_token(response.json())
        with allure.step('Удаляем созданного пользователя'):
            DeleteUser.delete_user(access_token)
        with allure.step('Проверяем, что "name", отправленный в запросе, и "name", полученный в теле ответа на запрос, совпадают'):
            assert name == name_response, f'"{name}", указанное в запросе, и "{name_response}", полученное в теле ответа на запрос, НЕ совпадают'


    @allure.title('Проверяем, что при регистрации уникального пользователя в теле ответа на запрос вернулcя "refreshToken"')
    def test_create_new_user_get_refresh_token(self, generate_user):
        with allure.step('Получаем ответ на создание уникального пользователя в виде словаря'):
            response_body = generate_user[1]
        with allure.step('Проверяем, что в теле ответа содержится ключ "refreshToken"'):
            assert KeyWords.REFRESH_TOKEN in response_body, f'В теле ответа отсутствует ключ {KeyWords.REFRESH_TOKEN}'
        with allure.step('Проверяем, что в ключе "refreshToken" содержатся какие-либо строковые значения'):
            assert (type(HelperMethods.is_key_in_response_body(response_body, KeyWords.REFRESH_TOKEN)) is str and
                    len(HelperMethods.is_key_in_response_body(response_body, KeyWords.REFRESH_TOKEN)) > 0), f'Данные в ответе на запрос в поле {KeyWords.REFRESH_TOKEN} представлены в неверном формате'


    @allure.title('Проверяем возможность создания пользователя, который уже зарегистрирован')
    def test_create_existing_user(self, generate_user):
        with allure.step('Получаем набор данных созданного уникального пользователя'):
            user_data = generate_user[0]
        with allure.step('Отправляем повторный запрос на создание уже существующего пользователя'):
            response = CreateUser.register_new_user(user_data)
        with allure.step('Проверяем, что код статуса ответа при созданиии существующего пользователя - 403'):
            HelperMethods.check_status_code(response, StatusCodes.FORBIDDEN)
        with allure.step('Проверяем, что в теле ответа содержится ключ "success" со значением "False" и присваиваем его переменной'):
            response_value = HelperMethods.is_key_in_response_body(response.json(), KeyWords.SUCCESS)
        with allure.step('Сравниваем фактическое значение ключа "success" в теле ответа с ожидаемым - "False"'):
            assert not response_value, f'Неверное значение ключа "{KeyWords.SUCCESS}" в теле ответа'
        with allure.step('Проверяем, что в теле ответа содержится ключ "message", получаем его значение и присваиваем его переменной'):
            response_message = HelperMethods.is_key_in_response_body(response.json(), KeyWords.MESSAGE)
        with allure.step('Сравниваем фактическое значение ключа "message" в теле ответа с ожидаемым'):
            assert response_message == RM.USER_EXISTS, f'Неверный текст поля {KeyWords.MESSAGE}'


    @allure.title('Проверяем невозможность создания уникального пользователя с одним из незаполненныз обязательных полей')
    @pytest.mark.parametrize('field_name', [
        KeyWords.EMAIL,
        KeyWords.PASSWORD,
        KeyWords.NAME
    ])
    def test_impossible_to_create_new_user_if_any_required_field_is_empty(self, field_name):
        with allure.step('Генерируем данные для создания нового уникального пользователя'):
            user_data = UserData.generate_new_user_data()
        with allure.step('Удаляем из сгенерированныж данных пользователя обязательное поле'):
            user_data.pop(field_name)
        with allure.step('Отправляем запрос на создание нового уникального пользователя'):
            response = CreateUser.register_new_user(user_data)
        with allure.step('Проверяем код статуса ответа при созданиии нового уникального пользователя без обязательного заполненного поля - 403'):
            HelperMethods.check_status_code(response, StatusCodes.FORBIDDEN)
        with allure.step('Проверяем, что в теле ответа содержится ключ "success" со значением "False" и присваиваем его переменной'):
            response_value = HelperMethods.is_key_in_response_body(response.json(), KeyWords.SUCCESS)
        with allure.step('Сравниваем фактическое значение ключа "success" в теле ответа с ожидаемым - "False"'):
            assert not response_value, f'Неверное значение ключа "{KeyWords.SUCCESS}" в теле ответа'
        with allure.step('Проверяем, что в теле ответа содержится ключ "message", получаем его значение и присваиваем его переменной'):
            response_message = HelperMethods.is_key_in_response_body(response.json(), KeyWords.MESSAGE)
        with allure.step('Сравниваем фактическое значение ключа "message" в теле ответа с ожидаемым'):
            assert response_message == RM.EMPTY_FIELDS, f'Неверный текст поля {KeyWords.MESSAGE}'
