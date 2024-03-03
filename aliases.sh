#!/bin/bash


addownership(){
    sudo chown -R zuser:zuser "$1"
}

prod(){
    docker-compose -f docker-compose.prod.yml "$@"
}

dcprodudb(){
    docker-compose -f docker-compose.prod.yml up -d --build
}

prodcollectstatic(){
    docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
}


prodrebuild(){
    docker-compose down -v
    docker-compose -f docker-compose.prod.yml up -d --build
    docker-compose -f docker-compose.prod.yml exec web python manage.py makemigrations --noinput
    docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
    docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
}

devcreatesu(){
    docker-compose  exec web python manage.py createsuperuser
}
devmigrate(){
    docker-compose  exec web python manage.py migrate --noinput
}

devmm(){
    docker-compose  exec web python manage.py makemigrations --noinput
}


devmanpy(){
    docker-compose  exec web python manage.py "$@"
}

devrebuild(){
    docker-compose down -v
    docker-compose up -d --build
    docker-compose exec web python manage.py makemigrations --noinput
    docker-compose exec web python manage.py migrate --noinput
    docker-compose exec web python manage.py collectstatic --no-input --clear
    docker-compose logs -f
}

devup(){
    docker-compose up -d
}