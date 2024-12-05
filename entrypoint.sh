#!/bin/bash

echo "Waiting for database to be ready..."
sleep 5

echo "Running migrations..."
python manage.py migrate --noinput

echo "Starting the application..."
exec "$@"