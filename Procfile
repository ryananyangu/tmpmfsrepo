release: python manage.py collectstatic --noinput
release: python manage.py makemigrations
release: python manage.py migrate
web: gunicorn --bind 0.0.0.0:$PORT mfs.wsgi:application --log-file -