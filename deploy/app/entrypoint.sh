#!/bin/bash

# Wait for postgres on host "db" and port "5432"
/wait-for-it.sh db:5432

# Once postgres has started, run migrations
python manage.py migrate

# Finally run the app with supervisor daemon using default.conf and including pos.supervisor.conf
/usr/bin/supervisord -n
