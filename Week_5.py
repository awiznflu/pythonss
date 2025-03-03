# Named blocks of code designed to do a specific job.
# Call a function to run the code.
# Functions are modular and can be called repeatedly each time
# # you need that specific job. More efficient
# a = 12
# b = "twenty five"
#
# print(a, b)
#
# def linear_line_function(slope, x_var, y_intercept):
#     y = slope * x_var + y_intercept
#     return y
#
# print()

def greet_user(): #function definition header
# Display a simple greeting.""“ # function body
    print("Hello!") # function body

greet_user() #Calling a function to run


### Can you write your own function displaying your name?
###
# def MyName_Display():
#     print("I am Inchan Hwang!")


def greet_user(username):
# """Display a simple greeting."""
    print(f"Hello, {str(username).title()}!")

greet_user('jesse')


# # def greet_user(username):
# # • username is a parameter that the function expects to be passed.
# # • It can be passed as a variable or a value.
# # • When calling the function, what is in () is called an argument
#

def describe_pet(animal_type, pet_name, gender):
    #two parameters
# """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"\nMy {animal_type}'s name is {pet_name.title()}.")
    print(f"This little baby is a {gender}.")


### Can you call a user defined function above
## while specifying function parameters
## so that Even if function argument order is reversed,
## the message display will look normal



# describe_pet('hamster', 'harry')
#                         # '#two arguments

def describe_pet(animal_type, pet_name): #two parameters
# """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry') #two arguments in a function call
describe_pet('dog', 'willie')

#
# def describe_pet(animal_type, pet_name): #two parameters
# # """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
#
#
#
# describe_pet('harry', 'hamster') #two arguments in a function call
# describe_pet('willie','dog')
#
# describe_pet(animal_type='hamster', pet_name='harry')
# describe_pet(pet_name='harry', animal_type='hamster')
#
#
# def describe_pet(pet_name, animal_type='dog'): #two parameters
# # """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
# describe_pet(animal_type='hamster', pet_name='harry')
# # '#order
# # doesn’t matter
# describe_pet(pet_name='willie')
#
#
# def describe_pet(pet_name, animal_type='dog'): #two parameters
# # """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
# # A dog named Willie.
# describe_pet('willie')
# describe_pet(pet_name='willie')
#
#
# def get_formatted_name(first_name, last_name):
# # """Return a full name, neatly formatted."""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
#
# musician = get_formatted_name('jimi', 'hendrix') #return value to
# # variable musician
# print(musician)
#
# def get_formatted_name(first_name, last_name, middle_name=''):
# # """Return a full name, neatly formatted."""
#     if middle_name:
#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name = f"{first_name} {last_name}"
#
#     return full_name.title()
#
# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)
# musician = get_formatted_name('john', 'hooker', 'lee')
# print(musician)