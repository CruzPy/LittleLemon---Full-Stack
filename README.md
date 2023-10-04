# LittleLemon---Full-Stack

Hi welcome to my final project for Meta's Backend Development Course.
To run this on your windows machine, first clone the project to your desired directory and follow the instructions below:

1. Activate the virtual environment: 'pipenv shell'
2. Install neccessary dependencies 'pipenv install'
3. Run the server 'python manage.py runserver'

## To test main functionaility, navigate to --> http://127.0.0.1:8000/
## To test API endpoints (Must have access) --> http://127.0.0.1:8000/api/menu or http://127.0.0.1:8000/api/bookings

## To use API endpoints with insomnia, please use this admin account:
Username: admin
Password: admin
Token-01a693272a238946b2d829ab0a50f6787a53f23a

## You could also register for new account:     # POST--> 'http://localhost:8000/auth/users/' -username -password -email (optional)
path('api-token-auth/', obtain_auth_token),     # POST -username -password
path('api/', include(router.urls)),

## Unit testing --> restaurant/tests.py
