from data import KeyWords
from order_methods import IngredientsData as ID


class HelperMethods:

    # Проверяем код ответа
    @staticmethod
    def check_status_code(response, expected_code):
        # Получаем код ответа
        received_code = response.status_code
        # Проверяем, что получен код ответа expected_code
        assert received_code == expected_code, f'Неверный код cтатуса в ответе: ожидаемый - "{expected_code}", фактический- "{received_code}"'


    # Проверяем наличие ключа в теле ответа
    @staticmethod
    def is_key_in_response_body(response, key):
        # Проверям, что в теле ответа присутствует ключ key
        assert key in response, f'В теле ответа отсутствует ключ "{key}"'
        # Возвращаем значение ключа key
        return response[key]


    # Проверяем наличие в теле ответа ключа "accessToken" и получаем его значение
    @staticmethod
    def get_access_token(response):
        # Проверяем наличие в теле ответа ключа "accessToken" и получаем его значение
        access_token = HelperMethods.is_key_in_response_body(response, KeyWords.ACCESS_TOKEN)
        # Проверяем, что тип авторизационного токена - строка, начинается со слова "Bearer " и его длина больше, чем длина слова "Bearer " c учетом пробела
        assert  (type(access_token) is str and
                KeyWords.ACCESS_TOKEN_TYPE in access_token and
                len(access_token) > len(KeyWords.ACCESS_TOKEN_TYPE)), f'Получено неверное значение ключа авторизационного токена {KeyWords.ACCESS_TOKEN}'
        return access_token


    # Получаем данные об ингредиентах
    @staticmethod
    def get_ingredients_list():
        # Отправляем запрос на получение данных об ингредиентах
        response = ID.get_ingredients_list()
        # Трансформируем полученный ответ в словарь
        response_list = response.json()
        # Проверяем, что в полученном словаре присутствует есть ключ "data" и возвращаем его значение в виде списка продуктов
        ingredients_list = HelperMethods.is_key_in_response_body(response_list, KeyWords.DATA)
        return ingredients_list


    # Получаем список булочек из списка ингредиентов
    @staticmethod
    def get_buns_list():
        # Инициализируем пустой список булочек
        buns_list = []
        # Назначаем переменную для списка из всех продуктов
        ingredients_list = HelperMethods.get_ingredients_list()
        # Выбираем в цикле из всего списка продуктов булочки и добавляем их в список булочек
        for item in ingredients_list:
            if item[KeyWords.TYPE] == KeyWords.BUN:
                buns_list.append(item)
        return buns_list


    # Получаем список начинок из списка ингредиентов
    @staticmethod
    def get_fillings_list():
        # Инициализируем пустой список начинок
        fillings_list = []
        # Назначаем переменную для списка из всех продуктов
        ingredients_list = HelperMethods.get_ingredients_list()
        # Выбираем в цикле из всего списка продуктов начинки и добавляем их в список начинок
        for item in ingredients_list:
            if item[KeyWords.TYPE] == KeyWords.FILLING:
                fillings_list.append(item)
        return fillings_list


    # Получаем список соусов из списка ингредиентов
    @staticmethod
    def get_sauces_list():
        # Инициализируем пустой список соусов
        sauces_list = []
        # Объявляем переменную для списка из всех продуктов
        ingredients_list = HelperMethods.get_ingredients_list()
        # Выбираем в цикле из всего списка продуктов coусы и добавляем их в список соусов
        for item in ingredients_list:
            if item[KeyWords.TYPE] == KeyWords.SAUCE:
                sauces_list.append(item)
        return sauces_list


    # Создаем бургер из двух булочек, двух начинок и двух соусов для проверки создания заказа
    @staticmethod
    def generate_burger():
        # Инициализируем пустой список для создания бургера
        burger = []
        # Получаем хеш булочки
        bun = HelperMethods.get_buns_list()[1][KeyWords.ID]
        # Добавляем в бургер две булочки
        burger.append(bun)
        burger.append(bun)
        # Получаем хеш начинок
        filling_1 = HelperMethods.get_fillings_list()[0][KeyWords.ID]
        filling_2 = HelperMethods.get_fillings_list()[1][KeyWords.ID]
        # Добавляем в бургер две начинки
        burger.append(filling_1)
        burger.append(filling_2)
        # Получаем хеш соусов
        sauce_1 = HelperMethods.get_sauces_list()[0][KeyWords.ID]
        sauce_2 = HelperMethods.get_sauces_list()[1][KeyWords.ID]
        # Добавляем в бургер два соуса
        burger.append(sauce_1)
        burger.append(sauce_2)
        # Возвращаем собранный бургер
        return burger
