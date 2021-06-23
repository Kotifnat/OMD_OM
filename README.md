# API OMD OM
1. Склонировать проект ```- git clone (либо ssh либо https)```
2. Установить виртуальное окружение (venv или pipenv)
3. Перейти в папку проекта
4. Установить зависимости```pip install -r requirements.txt``` 
или ```pipenv install```
5. Запустить ```python manage.py migrate```
7. Запустить  ```python manage.py loaddata data.json --app=api``` чтобы предзаполнить БД
8. Запустить сервер ```python manage.py runserver```
