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

The frontend is [here](https://github.com/percil/lots_vue) and here are the character sheet templates currently
supported by the Vue frontend:

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
    volumes:
      - type: bind
        source: .env.production
        target: /app/.env.production
```

And the `.env.rest` environment file:

```shell
export DJANGO_SECRET_KEY=<some_random_and_quite_string_including_exotic_stuff>
export REST_URL=<lorem-rest.ipsum.com>
export FRONT_URL=<lorem.ipsum.com>
```

And also the `.env.production` environment file:

```
VUE_APP_REST_API_URL=https://<lorem-rest.ipsum.com>/api
BASE_URL=https://<lorem.ipsum.com>
```

Please note that for both REST and front URLs, the HTTPS is set in the `settings/prod.py` file

# License (MIT)

Copyright © 2022 percil.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the “Software”), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

