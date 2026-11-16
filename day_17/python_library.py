# ---------------> Random Module <-----------

import random 

print(random.random())

print(random.randint(1, 30))

print(random.choice([1,3,8,9,'apple', 'banana', 'cherry']))


# ---------------> Math Module <-----------

import math

sqrt = math.sqrt(25)
print(sqrt)


pow = math.pow(2, 3)
print(pow)

factorial = math.factorial(5)
print(factorial)

ceil = math.ceil(4.2)
print(ceil)

floor = math.floor(4.2)
print(floor)
    
pi = math.pi
print(pi)

e = math.e
print(e)


# ---------------> Datetime Module <-----------

from datetime import datetime, timedelta

current_datetime = datetime.now() # Returns the current date and time
print(current_datetime)


converted_datetime = datetime.strptime("2023-10-15", "%Y-%m-%d")  # Convert string to datetime object
print(converted_datetime)


formatted_datetime = datetime.strftime(current_datetime, "%Y-%m-%d %H:%M:%S")  # Convert datetime object to string
print(formatted_datetime)

time_delta = current_datetime - timedelta(days = 10) # Calculate the time difference
print(time_delta)


# ---------------> Requests Module <-----------

import requests

response = requests.get('https://api.github.com')
print(response.status_code)  # Print the status code of the response
print(response.headers)  # Print the headers of the response