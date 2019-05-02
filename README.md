# Docker-compose django with batteries kit. All in one
This is docker-compose starter kit for webapp development.
Include:
- django
- rabbitmq
- celery + celery_beat
- redis
- raven(sentry)
- ssl via httpsify
- nginx
- postgres
- c9 for development in cloud

Almost production ready solution. 
Ask any questions in Issues.
Enjoy!

# To start
You need docker and docker-compose. Download project's folder, up project using:
> docker-compose up --build
and your server is ready.

Call 
> docker-compose up --build

again if you need to make migrations and migrate created models(automated on startup).
You can also do it manually:

> docker-compose exec app sh

> python3 manage.py makemigrations

and etc.

