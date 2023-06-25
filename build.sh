#!/bin/bash
set -o errexit  # exit on error

# Start the Celery worker
celery -A core worker --loglevel=info &

# Start the Celery beat scheduler
celery -A core beat --loglevel=info &

pip install -r requirements.txt

# Start the Django server
python manage.py collectstatic --no-input
python manage.py migrate
python manage.py create_traders

wait