#!/bin/bash

# Installing dependencies
echo "Installing dependencies"
pip install -r requirements.txt

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinputc

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Start server
echo "Starting server"
exec python manage.py runserver 0.0.0.0:8002 --insecure
