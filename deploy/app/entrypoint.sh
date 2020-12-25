#!/bin/bash

# Wait for postgres on host "db" and port "5432"
/wait-for-it.sh db:5432

django_migrate=${DJANGO_MIGRATE-no}
if [ "$django_migrate" == 'yes' ]; then
  # Once postgres has started, run migrations
  python manage.py migrate
  fi

start_app=${START_APP-yes}
if [ "$start_app" == 'yes' ]; then
  # Finally run the app with supervisor daemon using default.conf and including pos.supervisor.conf
  /usr/bin/supervisord -n
fi

echo "$@"
exec "$@" 1>&2