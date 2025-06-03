import convertapi
import os

convertapi.api_credentials = os.environ['API_TOKEN'] # your api token

# Retrieve user information
# https://www.convertapi.com/doc/user

print(convertapi.user())
