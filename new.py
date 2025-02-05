# Anna = 15
#
# num= int(input("Enter a number to divide by " + str(Anna) + ":"))
#
# Division = Anna/num
#
# print( str(Anna) + " divided by " + str(num) + " is " + str(Division))


# Chocolate = [ 'dark' , 'milk' , 'white' , ' toffee', 'hazelnut']
#
# print(Chocolate)
#
# print(Chocolate[-1].title())

countries = ['South Korea' , 'Columbia' , 'USA']

print (countries)

print ("\nI am from " + str(countries[0]))


countries[2] = "North Korea"

print ( countries[2])

countries.append('Serbia')

print ("\nNew item added to list: " + str(countries[3]))

print ("\n" + str(countries))

countries.append("Africa")

print ("\nI added a new element to the index: " + str(countries[4]))

print ("\n" + str (countries))

del countries[-1]

print ("\n" + str(countries))

not_where = 'Columbia'

countries.remove(not_where)

print ("\n" + str(countries))

print ("\n" +str(not_where) + " is too expensive")

countries.sort(reverse= False)

print (countries)