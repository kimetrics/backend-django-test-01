#!/bin/bash

# Wait for postgres on host "db" and port "5432"
/wait-for-it.sh ${DB_HOST}:5432

# Check if need migrations
django_migrate=${DJANGO_MIGRATE-False}
if [ "$django_migrate" == 'True' ]; then
  python manage.py migrate
  fi

# Run the app with supervisor daemon using default.conf and including pos.supervisor.conf
start_app=${START_APP-True}
if [ "$start_app" == 'True' ]; then
  /usr/bin/supervisord -n
fi

# Run conmmand passed to argument script
echo "$@"
exec "$@" 1>&2