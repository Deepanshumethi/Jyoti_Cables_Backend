#!/bin/sh

# Exit immediately if a command exits with a non-zero status.
set -e

# Collect static files
python3 manage.py collectstatic --noinput

# Apply database migrations
python3 manage.py migrate



