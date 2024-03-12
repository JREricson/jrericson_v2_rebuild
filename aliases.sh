#!/bin/bash

dkcleanup(){
    docker rm -v $(docker ps --filter status=exited -q 2>/dev/null) 2>/dev/null
    docker rmi $(docker images --filter dangling=true -q 2>/dev/null) 2>/dev/null
}

alias docker-compose='docker compose'

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

alias docker-compose='docker compose'

proxyrebuild(){
    docker-compose -f docker-compose.staging.yml down -v
    docker-compose -f docker-compose.staging.yml up -d --build
    docker-compose exec web python manage.py makemigrations --noinput
    docker-compose exec web python manage.py migrate --noinput
    docker-compose exec web python manage.py collectstatic --no-input --clear
    docker-compose logs -f
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

stagebackup(){
    docker-compose -f docker-compose.staging.yml exec web python manage.py dbbackup
}

prodbackup(){
    docker-compose -f docker-compose.prod.yml exec web python manage.py dbbackup
}

prodrebuild(){
    docker-compose -f docker-compose.prod.yml down -v
    docker-compose -f docker-compose.prod.yml up -d --build
    docker-compose exec web python manage.py makemigrations --noinput
    docker-compose exec web python manage.py migrate --noinput
    docker-compose exec web python manage.py collectstatic --no-input --clear
    docker-compose logs -f
}

