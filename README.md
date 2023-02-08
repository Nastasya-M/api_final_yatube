### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Nastasya-M/api_final_yatube
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
Примеры:

```
Для получения публикации нужно выполнить запрос:
GET/api/v1/posts/{id}/
Ответ:
{
"id": 0,
"author": "string",
"text": "string",
"pub_date": "2019-08-24T14:15:22Z",
"image": "string",
"group": 0
}
Для получения токена нужно выполнить запрос:
POST/api/v1/jwt/create/
{
"username": "string",
"password": "string"
}
Ответ:
400
{
"username": [
"Обязательное поле."
],
"password": [
"Обязательное поле."
]
}
Ответ:
200
{
"refresh": "string",
"access": "string"
}
