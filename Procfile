release: python manage.py makemigrations
release: python manage.py migrate
release: python manage.py makemigrations cordinates
release: python manage.py migrate cordinates
web: gunicorn --bind 0.0.0.0:$PORT mfs.wsgi:application --log-file -