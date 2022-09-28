
# API to Fetch Temperature

This API is responsible for retrieving the Minimum, Maximum, Average and the median temperatures for a specified city for the given number of days.

# Setup
1. Clone the project using the approach most flexible to you or simply downlod

2. Setup your virtual environment

3. cd to the project's root directory

4. Run the requirements.txt file using the following command

```
pip install -r requirements.txt
```
5. Run migrations





## Deployment

To deploy this project run

```bash
  python manage.py runserver
```


## Demo

1. Register a test user using the following url

/rest-auth/registration/

2. Generate access token using the link

/api/token/

3. Use the access token to query the weatherapi 
using the link

/api/locations/{city}/?number_of_days=4

## Running Tests

To run tests, run any of the following commands
based on your needs

```bash
  python manage.py test

  coverage run manage.py test

  coverage run manage.py test -v 2

  coverage run manage.py test -v 2 && coverage report

  coverage run --source "RESTAPI" manage.py test -v 2 && coverage report

  coverage run --source "RESTAPI" manage.py test -v 2 && coverage report && coverage html

```

