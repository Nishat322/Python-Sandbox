# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

# Sample JSON (pretend you are getting it from an outside api)

userJSON = '{"first_name": "John", "last_name":"Doe", "age": 30}'

# Parse to dictionary
user = json.loads(userJSON)
print(user)
print(user['first_name'])

car = {'make': 'Ford', 'model': 'Mustang', 'year': 1970}
carJSON = json.dumps(car) # make json object
print(carJSON)