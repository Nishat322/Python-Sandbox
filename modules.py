# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# import core python module 
import datetime
from datetime import date 
#import time
from time import time
# Pip modules
from camelcase import CamelCase
# import custom modules (like importing another js file)
from validator import validate_email

today = datetime.date.today() # date object is in datetime
today2 = date.today()
#timestamp = time.time()
timestamp2 = time()
print(today)
print(today2)
#print(timestamp)
print(timestamp2)

# Command Line pip3 install (package)
# pip3 freeze --> packages installed (installs globally)
c = CamelCase()
print(c.hump('hello there world'))

email = 'test#test.com'
if validate_email(email):
    print('Email is valid')
else: 
    print('Email is bad')





