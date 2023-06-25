#!/bin/bash
set -o errexit  # exit on error

python -m pip install --upgrade pip
pip install -r requirements.txt

# Start the Celery worker
celery -A core worker --loglevel=info &

# Start the Celery beat scheduler
celery -A core beat --loglevel=info &

# Start the Django server

python manage.py collectstatic
python manage.py migrate
python manage.py create_traders

wait