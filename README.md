# api_final_yatube
## Проект api_final позволяет:
   1. Подписываться на разных авторов.
   2. Просматривать, создавать, обновлять и удалять записи.
   3. Просматривать, создавать и удалять группы.
   4. Комментировать и удалять свои комментарии.

Документация по этому API доступна по URL-адресу: http://127.0.0.1:8000/redoc/
#
## Как установить и запустить проект:
Клонировать репозиторий к себе на машину:

<code> git clone https://github.com/Nizzerato/api_final_yatube.git </code>

<code> cd api_final_yatube </code>

Создать и активировать виртуальное окружение:

<code> python3 -m venv env </code>

<code> source env/bin/activate </code>

Установить зависимости из файла requirements.txt:

<code> python3 -m pip install --upgrade pip </code>

<code> pip install -r requirements.txt </code>

Выполнить миграции:

<code> python3 manage.py migrate </code>

Запустить проект:

<code> python3 manage.py runserver </code>
