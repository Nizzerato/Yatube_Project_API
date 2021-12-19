# api_final_yatube
## Проект api_final позволяет:
   1. Подписываться на разных авторов.
   2. Просматривать, создавать, обновлять и удалять записи.
   3. Просматривать, создавать и удалять группы.
   4. Комментировать и удалять свои комментарии.

Документация по этому API доступна по URL-адресу: http://127.0.0.1:8000/redoc/

***

## Как установить и запустить проект:
Клонировать репозиторий к себе на машину:

```
git clone https://github.com/Nizzerato/api_final_yatube.git
```

```
cd api_final_yatube
```

Создать и активировать виртуальное окружение:

```
python3 -m venv env
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
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
