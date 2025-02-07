### Question 1
### Can you make code to declare three variables,
### storing data such as 40, 55.44, 'I am the smartest person'?
from PIL.ImageChops import subtract

one = 34
two= 44
three = "This is cool"

print (one)
print(two)
print (three)


### Question 2
### Can you make code multiplying, adding, substracting, and
### dividing those two variables
### from Question 1?
product = one * two
print ("\n" + str(product))

divide = two/one
print ("\n" + str(divide))

minus = two - one
print ("\n" + str(minus))

add = one + two
print ("\n" + str(add))



### Question 3
### "Blood orange" · "Clementine" · "Mandarine" · "Tangerine" · "Papaya" ·
## "Passionfruit" · "Pawpaw" · "Peach" · "Pear"
### Can you make a code to define a list containing text string data above?

fruit = ['Blood Orange' , 'Clementine' , 'Mandarine' , 'Tangerine' , 'Papaya' , 'Passionfruit' , 'Pawpaw' , 'Peach' , 'Pear']


##Question 4
### Can you write python code printing a phrase "I eat fruit three times a day. These are "
### along with two elements in the list you wrote above?
### You must use the list along with index numbers.

print ("\nI eat fruit three times a day. These are " + str(fruit[1]) + ", " + str(fruit[3]) + ", and " + str(fruit[-4]) + ".")

###Question 5
### Can you replace 4th and 6th element with "Citron" and "Crab apple"?
fruit[3] = 'Citron'
fruit[5] = 'Crab apple'

### Question 6
### Can you simply add a new element "Gooseberry" in the list?

fruit.append('Gooseberry')

print ("\n" + str(fruit[-1]))


### Question 7
### Can you insert a new element "Juniper berry" in the index 5?
fruit.insert(4, 'Juniper berry')
print ("\n" + str(fruit[4]))

### Quetion 8
### Can you remove the element in the index no. 2?
del fruit[1]


### Question 9
### Can you write a python code to sort elements in the list you created in Question 3?
fruit.sort(reverse= False)

print ("\n" + str(fruit))
