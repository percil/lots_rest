# Lord of the Sheets

The project is the administration interface and the REST API for the Lord of the Sheets web application.
It is written in Python using [Django](https://www.djangoproject.com/) framework.

## Installation

1. Create your virtual environment: `python -m venv venv`
2. Activate it: `source venv/bin/activate`
3. Install the dependencies: `pip -r requirements.txt`
4. Create the database: `python ./manage.py migrate`
5. Create the first user: `python ./manage.py createsuperuser`
6. Enjoy: `python ./manage.py runserver`

You may also create a docker image: `docker build -t <whatever_name_you_want_to_give> .`

## Endpoints

- `/admin` the administration interface
- `/api/sessions` for retrieving the game sessions
- `/api/sheets/<slug>` for retrieving and updating the character sheet

## Frontend integration

Here are the character sheet templates currently supported by the Vue frontend:

- Whitebox (code: whitebox)
- Freaks'Squeele (code: freaks-squeele)

## Using docker-compose

Here is a `docker-compose.yml` sample to ease your life:

```yaml
version: '2'

services:

  lots-rest:
    image: percil/lots-rest
    restart: always
    ports:
      - "127.0.0.120:8001:8000"
    env_file:
      - .env.rest
    volumes:
      - type: bind
        source: /var/opt/lots/files/db.sqlite3
        target: /app/db.sqlite3

  lots:
    image: percil/lots
    restart: always
    ports:
      - "127.0.0.120:8081:8080"
```

And the `.env.rest` environment file:

```shell
export DJANGO_SECRET_KEY=<some_random_and_quite_string_including_exotic_stuff>
export REST_URL=<lorem-rest.ipsum.com>
export FRONT_URL=<lorem.ipsum.com>
```

Please note that for both REST and front URLs, the HTTPS is set in the `settings/prod.py` file
