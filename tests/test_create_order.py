import allure

from data import KeyWords, StatusCodes, ResponseMessages as RM
from generators import generate_invalid_ingredient_hash
from helper_methods import HelperMethods
from order_methods import CreateOrder




class TestCreateOrder:

    @allure.title('Проверяем возможность создания авторизованным пользователем заказа с ингредиентами')
    def test_create_by_authorized_user_new_order_with_ingredients_successfully(self, generate_user):
        with allure.step('Получаем "accessToken" зарегистрированного уникального пользователя'):
            access_token = generate_user[2]
        with allure.step('Создаем бургер для оформления заказа'):
            burger = HelperMethods.generate_burger()
        with allure.step('Отправляем запрос на создание заказа'):
            response = CreateOrder.make_order(burger, headers={KeyWords.AUTH_FIELD: access_token})
        with allure.step('Проверяем статус полученного ответа - 200'):
            HelperMethods.check_status_code(response, StatusCodes.OK)
        with allure.step('Проверяем, что в теле ответа содержится ключ "success" и присваиваем его значение переменной'):
            response_value = HelperMethods.is_key_in_response_body(response.json(), KeyWords.SUCCESS)
        with allure.step('Сравниваем фактическое значение ключа "success" в теле ответа с ожидаемым - "True"'):
            assert response_value, f'Неверное значение ключа "{KeyWords.SUCCESS}" в теле ответа'
        with allure.step('Проверяем, что в теле ответа содержится ключ "name" и присваиваем его значение переменной'):
            order_name = HelperMethods.is_key_in_response_body(response.json(), KeyWords.NAME)
        with allure.step('Проверяем, что фактическое значение ключа "name" представлено в виде строкового типа данных'):
            assert type(order_name) is str, f'Неверный формат значения ключа "{KeyWords.NAME}" в теле ответа'
        with allure.step('Проверяем, что в теле ответа содержится ключ "order" и присваиваем его значение переменной'):
            order_list = HelperMethods.is_key_in_response_body(response.json(), KeyWords.ORDER)
        with allure.step('Проверяем, что фактическое значение ключа "name" представлено в виде cловаря'):
            assert type(order_list) is dict, f'Неверный формат значения ключа "{KeyWords.ORDER}" в теле ответа'
        with allure.step('Проверяем, что в теле ответа в словаре по ключу "order" содержится ключ "number" и присваиваем его значение переменной'):
            order_number = HelperMethods.is_key_in_response_body(order_list, KeyWords.NUMBER)
        with allure.step('Проверяем, что фактическое значение ключа "number" - число'):
            assert str(order_number).isdigit(), f'Неверный формат значения ключа "{KeyWords.NUMBER}" в теле ответа'


    @allure.title('Проверяем возможность создания авторизованным пользователем заказа без ингредиентов')
    def test_create_by_authorized_user_new_order_without_ingredients(self, generate_user):
        with allure.step('Получаем "accessToken" зарегистрированного уникального пользователя'):
            access_token = generate_user[2]
        with allure.step('Создаем пустой бургер для оформления заказа'):
            burger = []
        with allure.step('Отправляем запрос на создание заказа'):
            response = CreateOrder.make_order(burger, headers={KeyWords.AUTH_FIELDE: access_token})
        with allure.step('Проверяем статус полученного ответа - 400'):
            HelperMethods.check_status_code(response, StatusCodes.BAD_REQUEST)
        with allure.step('Проверяем, что в теле ответа содержится ключ "success" и присваиваем его значение переменной'):
            response_value = HelperMethods.is_key_in_response_body(response.json(), KeyWords.SUCCESS)
        with allure.step('Сравниваем фактическое значение ключа "success" в теле ответа с ожидаемым - "False"'):
            assert not response_value, f'Неверное значение ключа "{KeyWords.SUCCESS}" в теле ответа'
        with allure.step('Проверяем, что в теле ответа содержится ключ "message" и присваиваем его значение переменной'):
            response_message = HelperMethods.is_key_in_response_body(response.json(), KeyWords.MESSAGE)
        with allure.step('Сравниваем, что текст сообщения об ошибке соответствует ожидаемому - "Ingredient ids must be provided"'):
            assert response_message == RM.BURGER_WITH_NO_INGREDIENTS, f'Неверный текст поля {KeyWords.MESSAGE}'


    @allure.title('Проверяем возможность создания неавторизованным пользователем заказа с ингредиентами')
    def test_create_by_unauthorized_user_new_order_with_ingredients_successfully(self):
        with allure.step('Создаем бургер для оформления заказа'):
            burger = HelperMethods.generate_burger()
        with allure.step('Отправляем запрос на создание заказа'):
            response = CreateOrder.make_order(burger)
        with allure.step('Проверяем статус полученного ответа - 200'):
            HelperMethods.check_status_code(response, StatusCodes.OK)
        with allure.step('Проверяем, что в теле ответа содержится ключ "success" и присваиваем его значение переменной'):
            response_value = HelperMethods.is_key_in_response_body(response.json(), KeyWords.SUCCESS)
        with allure.step('Сравниваем фактическое значение ключа "success" в теле ответа с ожидаемым - "True"'):
            assert response_value, f'Неверное значение ключа "{KeyWords.SUCCESS}" в теле ответа'
        with allure.step('Проверяем, что в теле ответа содержится ключ "name" и присваиваем его значение переменной'):
            order_name = HelperMethods.is_key_in_response_body(response.json(), KeyWords.NAME)
        with allure.step('Проверяем, что фактическое значение ключа "name" представлено в виде строкового типа данных'):
            assert type(order_name) is str, f'Неверный формат значения ключа "{KeyWords.NAME}" в теле ответа'
        with allure.step('Проверяем, что в теле ответа содержится ключ "order" и присваиваем его значение переменной'):
            order_list = HelperMethods.is_key_in_response_body(response.json(), KeyWords.ORDER)
        with allure.step('Проверяем, что фактическое значение ключа "name" представлено в виде cловаря'):
            assert type(order_list) is dict, f'Неверный формат значения ключа "{KeyWords.ORDER}" в теле ответа'
        with allure.step('Проверяем, что в теле ответа в словаре по ключу "order" содержится ключ "number" и присваиваем его значение переменной'):
            order_number = HelperMethods.is_key_in_response_body(order_list, KeyWords.NUMBER)
        with allure.step('Проверяем, что фактическое значение ключа "number" - число'):
            assert str(order_number).isdigit(), f'Неверный формат значения ключа "{KeyWords.NUMBER}" в теле ответа'


    @allure.title('Проверяем возможность создания неавторизованным пользователем заказа без ингредиентов')
    def test_create_by_authorized_user_new_order_without_ingredients(self):
        with allure.step('Создаем пустой бургер для оформления заказа'):
            burger = []
        with allure.step('Отправляем запрос на создание заказа'):
            response = CreateOrder.make_order(burger)
        with allure.step('Проверяем статус полученного ответа - 400'):
            HelperMethods.check_status_code(response, StatusCodes.BAD_REQUEST)
        with allure.step('Проверяем, что в теле ответа содержится ключ "success" и присваиваем его значение переменной'):
            response_value = HelperMethods.is_key_in_response_body(response.json(), KeyWords.SUCCESS)
        with allure.step('Сравниваем фактическое значение ключа "success" в теле ответа с ожидаемым - "False"'):
            assert not response_value, f'Неверное значение ключа "{KeyWords.SUCCESS}" в теле ответа'
        with allure.step('Проверяем, что в теле ответа содержится ключ "message" и присваиваем его значение переменной'):
            response_message = HelperMethods.is_key_in_response_body(response.json(), KeyWords.MESSAGE)
        with allure.step('Сравниваем, что текст сообщения об ошибке соответствует ожидаемому - "Ingredient ids must be provided"'):
            assert response_message == RM.BURGER_WITH_NO_INGREDIENTS, f'Неверный текст поля {KeyWords.MESSAGE}'


    @allure.title('Проверяем создание заказа с неверным хешем ингредиентов')
    def test_create_new_order_with_invalid_ingredients_hash(self):
        with allure.step('Создаем бургер с неверным хешем ингредиентов'):
            burger = [generate_invalid_ingredient_hash()]
        with allure.step('Отправляем запрос на создание заказа'):
            response = CreateOrder.make_order(burger)
        with allure.step('Проверяем статус полученного ответа - 500'):
            HelperMethods.check_status_code(response, StatusCodes.ERROR_500)
