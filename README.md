Dev Notes
=========

### Flask App

This flask app is based on the cookiecutter template, [Flask Foundation](https://github.com/JackStouffer/Flask-Foundation.git)

##### Initialization

1. Run required services first:

    `docker-compose up`

2. On first run, create your local virtualenv:

    `make env`

2. Activate local virtualenv:

    `source env/bin/activate`

3. Run the flask app:

    `./manage.py server`

4. Preview in browser: http://127.0.0.1:5000

##### Shutting down

1. `CTRL + C` in the flask app console

2. `deactivate` your virtualenv

3. Stop required services:

    `docker-compose stop`

##### Other commands

1. Execute unit tests:

    `make test`

2. Execute code linting tool:

	`make lint`

3. Clean slate:

    `make clean deps`