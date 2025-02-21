# animal = 'cat'
# print ("Is animal == 'cat'? I predict True.")
# print (animal == 'cat')
#
# print ("\nIs animal == 'dog'? I predict False")
# print (animal =='dog')
#
# car = 'mercedes'
# print ("Is car == 'mercedes'? I predict True.")
# print (car == 'mercedes')
#
# print ("\nIs car == 'toyota'? I predict False")
# print (car =='toyota')
#
# country = 'USA'
# print ("Is country== 'USA'? I predict True.")
# print (country == 'USA')
#
# print ("\nIs country == 'Serbia'? I predict False")
# print (country =='Serbia')
#
# dino = 'trex'
# print ("Is dino == 'trex'? I predict True.")
# print (dino == 'trex')
#
# print ("\nIs dino == 'raptor'? I predict False")
# print (dino =='raptor')
#
# chocolate = 'dark'
# print ("Is chocolate == 'dark'? I predict Yes.")
# print (chocolate == 'dark')
#
# print ("\nIs chocolate == 'white'? I predict No")
# print (chocolate =='white')

# print ("Test one checking inequality and equality")
# print ('hello' == 'world')
# print ('hello' == 'hello')
#
# print ("Test two checking lower")
# print ('HELLO'.lower() == 'hello')
# print ('HELLO'.lower() == 'HELLO')
#
# print ("test 3: Number testing")
# print (10 >5)
# print (10 <5)
#
# print ("test 4: and")
# print (10 >5 and 20 > 4)
# print (10 <5 and 20 > 4)
#
# print ("test 5: or")
# print (10 >5 or 20 > 4)
# print (10 <5 or 20 > 4)
#
#
# print ("test 6: not in list")
# fruit = ['banana' , 'apple' , 'kiwi']
# print ('banana' in fruit)
# print ('orange' in fruit)
#
# print ("test 7: in list")
# print ('banana' in fruit)
# print ('kiwi' in fruit)
#

favorite_languages = {
    'jen': ['python' , 'rust'],
    'sarah' : ['c'] ,
    'edward' : ['rust' , 'go'] ,
    'phil' : ['python' , 'haskell'],
    }
print ("The following languages have been mentioned:")
for name in favorite_languages.keys():
    print (name.title())

favorite_languages = input("What is your name so we can see what language you like.")
if f'{favorite_languages}' not in favorite_languages.keys():
    print ('Joss please take our poll')
