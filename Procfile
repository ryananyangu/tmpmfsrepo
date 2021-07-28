release: python manage.py makemigrations cordinates
release: python manage.py migrate cordinates
release: python manage.py collectstatic --noinput
web: gunicorn --bind 0.0.0.0:$PORT mfs.wsgi:application --log-file -