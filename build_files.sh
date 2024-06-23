#!/bin/sh

# Exit immediately if a command exits with a non-zero status.
set -e

# Collect static files
python manage.py collectstatic --noinput

# Apply database migrations
python manage.py migrate


pip install -r requirements.txt
python3.9 manage.py collectstatic


