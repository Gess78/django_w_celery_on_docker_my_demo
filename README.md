

docker-compose up -d --build 

docker-compose up -d   

docker exec -it django_w_celery_on_docker_my_demo_web_1 python  manage.py createsuperuser

docker-compose logs -f 

docker-compose down 