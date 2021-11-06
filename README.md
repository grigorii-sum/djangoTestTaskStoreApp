# djangoTestTaskStoreApp
Проект "djangoTestTaskStoreApp" является одним из двух приложений для решения тестовой задачи.

Задача заключается в том, чтобы реализовать двустороннюю синхронизацию данных между двумя приложениями посредством REST API (следовательно, добавление/изменение/удаление информации посредством http-запросов).

---

Приложение Store App (djangoTestTaskStoreApp) имеет следующий функционал:

- http://127.0.0.1:8001/store-order/create/ - создание StoreOrder и отправка запроса на создание WarehouseOrder
- http://127.0.0.1:8001/store-order/update/<str:pk>/ - изменение StoreOrder и отправка запроса на изменение WarehouseOrder
- http://127.0.0.1:8001/store-order/update-from-warehouse/<str:pk>/ - метод для изменения StoreOrder (запрос на изменение приходит от Warehouse App при изменении WarehouseOrder)
- http://127.0.0.1:8001/store-order/delete/<str:pk>/ - удаление StoreOrder и отправка запроса на удаление WarehouseOrder
- http://127.0.0.1:8001/store-order/detail/<str:pk>/ - просмотр StoreOrder

---

## ЗАПУСК ПРОЕКТА

Введите последовательно все нижеперечисленные команды:

`virtualenv venv`

`source venv/bin/activate`

`pip install -r requirements.txt`

`python3 manage.py migrate`

`python3 manage.py runserver 8001`

Проект запущен.
