# stripe - проект с отработкой для подключения платежей stripe.

## Описание проекта:
Магазин, где на главную старницу выводится список всех доступных покупок, на ней можно перейти в подкатегории и узнать 
о продукте больше и оплатить в системе Stripe.
Проект развернут в трех docker контейнерах в Яндекс облаке. Адрес проекта 
```
http://158.160.10.19/  
```
## Основные эндпоинты:
Получить список всех продуктов.
```
http://158.160.10.19/
```
Просмотр описания товаров.
```
http://158.160.10.19/item/<id>
```
Установление сеанса с Stripe.
```
http://158.160.10.19/buy/<id>
```
## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/vladimirramozin/stripe.git
```
Создать файл .env в корне проекта. Со следующим содержанием:
```
STRIPE_PRIVATE_KEY=
DB_ENGINE=django.db.backends.postgresql
DB_NAME=
POSTGRES_USER=
POSTGRES_PASSWORD=
DB_HOST=
DB_PORT=5432
DOMAIN=http://127.0.0.1:8000
```
Перейти в папку stripe собрать и запустить докер образ:
```
sudo docker-compose up -d --build
```

Выполнить миграции и собрать статику:
```
sudo docker-compose exec web python manage.py migrate
sudo docker-compose exec web python manage.py createsuperuser
sudo docker-compose exec web python manage.py collectstatic --no-input 
```


## Системные требования:
asgiref==3.5.2
certifi==2022.9.14
charset-normalizer==2.1.1
Django==3.2.15
gunicorn==20.1.0
idna==3.4
psycopg2-binary==2.9.3
python-dotenv==0.21.0
pytz==2022.2.1
requests==2.28.1
sqlparse==0.4.2
stripe==4.1.0
tzdata==2022.2
urllib3==1.26.12
