## Дипломный проект. Задание 2: Автотесты для API Stellar Burgers

## Студент: Алексей Горячев

## <h>Когорта: #26+27</h>
<hr>

## <h>Инструкция по запуску:</h>

### <h>1. Установите зависимости:</h>

> pip install -r requirements.txt</h>

### <h>2. Запустить все тесты и записать отчет:</h>

> pytest --alluredir=./allure-results

### <h>3. Посмотреть отчет по прогону html</h>

> allure serve ./allure-results


<hr>

<h3 align="left" style="color:yellow">Project files and description:</h3>

| Название файла       | Содержание файла                                  |
|----------------------|---------------------------------------------------|
| allure-results.dir   | Папка с отчетами Allure                           |                                                               |
| tests                | Директория с тестами                              |
| conftest.py          | Фикстуры                                          |
| test_create_order.py | Тесты для создания заказа                         |
| test_create_user.py  | Тесты на создание пользователя                    |
| test_login_user.py   | Тесты на логин пользователя                       |
| .gitignore           | Файл .gitignore                                   |
| data.py              | Файл с url-ами и дополнительными данными          |
| generators.py        | Файл для генерации тестовых данных                
| helper_methods.py    | Файл со вспомогательными методами для тестов      |
| order_methods.py     | Файл с методами для тестирования создания заказов |
| README.md            | README-файл                                       |
| requirements.txt     | Файл с зависимостями                              |        
| user_methods.py      | Файл с методами для тестирования пользователя     |