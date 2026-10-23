#!/bin/bash

dkcleanup() {
    docker rm -v $(docker ps --filter status=exited -q 2>/dev/null) 2>/dev/null
    docker rmi $(docker images --filter dangling=true -q 2>/dev/null) 2>/dev/null
}

alias docker-compose='docker compose'

addownership() {
    sudo chown -R "$USER:$USER" "$1"
}

prod() {
    docker-compose -f docker-compose.prod.yml "$@"
}

stage() {
    docker-compose -f docker-compose.staging.yml "$@"
}

dcprodudb() {
    prod up -d --build
}

prodcollectstatic() {
    prod exec web python manage.py collectstatic --no-input --clear
}

devcreatesu() {
    docker-compose exec web python manage.py createsuperuser
}

devmigrate() {
    docker-compose exec web python manage.py migrate --noinput
}

devmm() {
    docker-compose exec web python manage.py makemigrations --noinput
}

devmanpy() {
    docker-compose exec web python manage.py "$@"
}

devlint() {
    # root: bind-mounted files are owned by the host user
    docker-compose exec -u root web black .
    docker-compose exec -u root web flake8 .
}

devtest() {
    docker-compose exec -u root web pytest -p no:cacheprovider
}

proxyrebuild() {
    # stage down -v
    stage up -d --build
    stage exec web python manage.py migrate --noinput
    stage exec web python manage.py collectstatic --no-input --clear
    stage logs -f
}

devrebuild() {
    # docker-compose down -v
    docker-compose up -d --build
    docker-compose exec web python manage.py makemigrations --noinput
    docker-compose exec web python manage.py migrate --noinput
    docker-compose exec web python manage.py collectstatic --no-input --clear
    docker-compose logs -f
}

devup() {
    docker-compose up -d
}

stagebackup() {
    stage exec web python manage.py dbbackup
}

prodbackup() {
    prod exec web python manage.py dbbackup
}

prodrestore() {
    echo y | prod exec -T web python manage.py dbrestore
}

stagerestore() {
    echo y | stage exec -T web python manage.py dbrestore
}

prodrebuild() {
    # prod down -v
    prod up -d --build
    prod exec web python manage.py migrate --noinput
    prod exec web python manage.py collectstatic --no-input --clear
    # prodrestore
    prod logs -f
}

transfertoServer() {
    # trailing slash on source = copy contents into jrericson/, not a nested jrericson_v2/
    rsync -avzh /home/puser/programming/websites/jrericson_v2/ \
      --exclude app/venv \
      --exclude .git \
      mywebsite:jrericson/
}
