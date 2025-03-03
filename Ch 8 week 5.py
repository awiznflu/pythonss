# this is 8-14
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('Anna', 'Weissenfluh',
                             location='North Carolina',
                             field='Cybersecurity')
print(user_profile)

# 1. import module_name
import my_function
print(my_function.greet("Kat"))

# 2. from module_name import function_name
from my_function import greet
print(greet("Robert"))

# 3. from module_name import function_name as fn
from my_function import greet as fn
print(fn("Skylar"))

# 4. import module_name as mn
import my_function as mn
print(mn.greet("Shelia"))

# 5. from module_name import *
from my_function import *
print(greet("Mary"))