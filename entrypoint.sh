#!/bin/bash


echo "Apply database migrations"; python manage.py migrate;
echo "Create Superuser";python manage.py createsuperuser --no-input;
echo "Collect static files";python manage.py collectstatic --noinput;
echo "Starting server"; python manage.py runserver 0.0.0.0:8000
