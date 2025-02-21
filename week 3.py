# cars = 'BMW'
#
# 'bmw' != 'Bmw'
# 'bmw' != 'BMW'
#
# if cars.lower() == 'bmw':
#     print (cars.upper())
#     print ('Wow they are different')
#
# if cars == 'altima':
#     print("They are the same ")
# else:
#     print ('They are not the same')

# age = 17
#
# if age <= 18:
#     print ('You are underage')
# else:
#     print ('You are able to work')

# age1= 18
# age2 = 21
#
# if age1 >= 17 and age2 >= 21:
#     print ('True')
# else:
#     print('False')
#

toppings= ['mushrooms' , 'sausage' , 'olives']
# if 'olives' in toppings:
#     print ('True')
# else:
#     print ('False')

# if 'apple' in toppings:
#     print ('True')
# else:
#     print ('That is not a topping')

users= ['Poppy' , 'Amy' , 'Josh']

# if 'Jack' in users:
#     print ('You can post')
# else:
#     print ('You cannot post')
# if 'Jack' not in users:
#     users.append('Jack')
#     print ('\n' + str(users[-1]) + " was added to the list")
# else:
#     print ('\nThat user alreaqdy exists')

colors= {'4' : 'green' , 5: 'red', 'points': 5}
print (colors[5])
colors ['Student ID'] = '220572'
print (colors)

colors ['points'] = 10
print ('New points:', {colors['points']})