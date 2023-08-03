#!/bin/sh

# Check the command argument and run the appropriate command
if [ "$1" = "runserver" ]; then
    # Run Django development server
    python manage.py runserver 0.0.0.0:$DJANGO_DEV_SERVER_PORT

elif [ "$1" = "gunicorn" ]; then
    # Run Gunicorn server
    exec "$@"

else
    # If the command is not recognized, print an error message
    echo "Unknown command: $1"
    exit 1
fi
