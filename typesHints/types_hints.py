'''
 
Type hints are a special syntax that allows declaring the type 
of a variable, we use this to have more suport from editors and
tools.

'''

# with type hints

def get_full_name(first_name: str, last_name: str):
    full_name  = first_name.title() + ' ' + last_name.title()
    return full_name

print(get_full_name('werisson', 'felix'))

# without type hints: def get_full_name(first_name, last_name):

''' 
When we adding type hints, nothing normally change what happens
from what would happen without them.

It's for suport us for creating functions.

But, there are more usefull thing: errors checks:

'''

def get_name_with_age(name: str, age: int):
    name_with_age = name + "is this old: " + str(age)
    return name_with_age


print(get_name_with_age('werisson', 18))



''' 

We can use to type hints for declarete parameters 
as imported function

'''

from typing import Any

def some_function(data: Any):
    print(data)

