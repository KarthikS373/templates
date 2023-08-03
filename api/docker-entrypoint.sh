#!/bin/sh

# Wait for the database to be ready before running the Django application
# until PGPASSWORD=$POSTGRES_PASSWORD psql -h db -U $POSTGRES_USER -d $POSTGRES_DB -c '\l' > /dev/null 2>&1; do
#     echo "Waiting for the database to be ready..."
#     sleep 2
# done

# Apply database migrations (if any)
python manage.py migrate --noinput

# Create a superuser if there are no users in the database
#!/bin/sh

# Check if the superuser should be created
if [ "$CREATE_SUPERUSER" = "yes" ]; then
    # Apply database migrations (if any)
    python manage.py migrate --noinput

    # Check if superuser exists (username is used as the identifier for the superuser)
    if [ -z "$(python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='$DJANGO_SUPERUSER_USERNAME').exists()")" ]; then
        # Create the superuser with the specified values
        python manage.py createsuperuser --noinput --username "$DJANGO_SUPERUSER_USERNAME" --email "$DJANGO_SUPERUSER_EMAIL"
        echo "Superuser '$DJANGO_SUPERUSER_USERNAME' created."
    else
        echo "Superuser '$DJANGO_SUPERUSER_USERNAME' already exists. Skipping creation."
    fi

    # Collect static files
    python manage.py collectstatic --noinput

    # Disable superuser creation for subsequent runs (e.g., Celery)
    export CREATE_SUPERUSER="no"
fi

# Start Gunicorn server or other service (e.g., Celery worker/beat)
exec "$@"



# Collect static files
python manage.py collectstatic --noinput

# Start Gunicorn server
exec "$@"
