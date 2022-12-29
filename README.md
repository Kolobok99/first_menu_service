Menu Service v1
---
Техническое задание
---
<a href="https://uptraderio-my.sharepoint.com/personal/d_sokolova_uptrader_io/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fd%5Fsokolova%5Fuptrader%5Fio%2FDocuments%2F%D0%A2%D0%B5%D1%81%D1%82%D0%BE%D0%B2%D0%BE%D0%B5%20Python%2Epdf&parent=%2Fpersonal%2Fd%5Fsokolova%5Fuptrader%5Fio%2FDocuments&ga=1">ТЗ</a>

Системные требования
---
- Windows / Linux / MacOS
- Docker
- Docker-compose

Стек 
---
- Python
- Django
- PostgreSQL
- Docker, docker-compose

Зависимости
---
- Django==4.1.3
- psycopg2==2.9.5
- django-debug-toolbar==3.8.1
- django-mptt==0.14.0
- django-nested-admin==4.0.2

Запуск проекта
---
1.  Клонировать проект и перейти в его корень:

		git clone https://github.com/Kolobok99/first_menu_service
		cd first_menu_service

2. Собрать проект

		cd docker-composes
		docker compose build

6. Запустить проект

		docker compose up



