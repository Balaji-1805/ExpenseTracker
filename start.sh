#!/bin/bash

# Exit on any error
set -e

# Step 1: Activate virtual environment (if you're using one)
# Uncomment the line below if you're using a virtual environment
# source /path/to/your/virtualenv/bin/activate

# Step 2: Install dependencies (useful for new environments)
pip install -r requirements.txt

# Step 3: Collect static files for production
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Step 4: Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Step 5: Start the Gunicorn server
echo "Starting Gunicorn server..."
gunicorn --workers 3 --bind 0.0.0.0:8000 ExpenseTracker.wsgi:application
