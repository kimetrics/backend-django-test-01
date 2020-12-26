#!/bin/bash

# Wait for postgres
/wait-for-it.sh ${DB_HOST}:${DB_PORT}

# Check if need migrations
django_migrate=${DJANGO_MIGRATE-False}
if [ "$django_migrate" == 'True' ]; then
  echo "Making migrations..."
  python manage.py migrate
fi

python manage.py collectstatic --noinput


# Run the app with supervisor daemon using default.conf and including pos.supervisor.conf
start_app=${START_APP-True}
if [ "$start_app" == 'True' ]; then
  echo "Starting supervisord..."
  echo "Running on port $PORT"
  /usr/bin/supervisord -n -c /etc/supervisor/conf.d/pos.supervisor.conf
fi

# Run conmmand passed to argument script
echo "$@"
exec "$@" 1>&2