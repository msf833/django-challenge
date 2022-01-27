# django-challenge


The volleyball Federation decided to use an online selling platform for the next season, and our company has been chosen for implementing that.

# Requirements

Our system should have REST APIs for the following tasks:

- User signup and login
- Adding a new stadium
- Defining matches
- Defining the place of seats for each match
- Buying seats of a match (There is no need for using a payment gateway)

# solution
Added Stadium , Matches and ticket models to manage and implement management system .
Used DRF django rest framework to implement APIs , also use different packages for documents like swagger and redoc to support openapi.

# Implemented
1. Stadium mangement API
2. matches management API and seats
3. Ticket management API 
4. User Auth
5. User Register
6. Forgot Password API

# Database 
sqlie used for db , you can change it from settings !

# installation
1. create your virtual env
2. pip install -r requirements.txt
3. run migrate
4. run server 
