animal = 'cat'
print ("Is animal == 'cat'? I predict True.")
print (animal == 'cat')

print ("\nIs animal == 'dog'? I predict False")
print (animal =='dog')

car = 'mercedes'
print ("Is car == 'mercedes'? I predict True.")
print (car == 'mercedes')

print ("\nIs car == 'toyota'? I predict False")
print (car =='toyota')

country = 'USA'
print ("Is country== 'USA'? I predict True.")
print (country == 'USA')

print ("\nIs country == 'Serbia'? I predict False")
print (country =='Serbia')

dino = 'trex'
print ("Is dino == 'trex'? I predict True.")
print (dino == 'trex')

print ("\nIs dino == 'raptor'? I predict False")
print (dino =='raptor')

chocolate = 'dark'
print ("Is chocolate == 'dark'? I predict Yes.")
print (chocolate == 'dark')

print ("\nIs chocolate == 'white'? I predict No")
print (chocolate =='white')

print ("Test one checking inequality and equality")
print ('hello' == 'world')
print ('hello' == 'hello')

print ("Test two checking lower")
print ('HELLO'.lower() == 'hello')
print ('HELLO'.lower() == 'HELLO')

print ("test 3: Number testing")
print (10 >5)
print (10 <5)

print ("test 4: and")
print (10 >5 and 20 > 4)
print (10 <5 and 20 > 4)

print ("test 5: or")
print (10 >5 or 20 > 4)
print (10 <5 or 20 > 4)


print ("test 6: not in list")
fruit = ['banana' , 'apple' , 'kiwi']
print ('banana' in fruit)
print ('orange' in fruit)

print ("test 7: in list")
print ('banana' in fruit)
print ('kiwi' in fruit)


favorite_languages = {
    'jen': {'languages': ['python' , 'rust'], 'proficiency': ['beginner' , 'intermediate']},
    'sarah' :{'languages': ['c'] , 'proficiency':['advanced']},
    'edward' : {'languages':['rust' , 'go'] , 'proficiency': ['intermediate' , 'intermediate']},
    'phil' : {'languages': ['python' , 'haskell'], 'proficiency': ['advanced' , 'intermediate']},
    }
for name, info in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages and proficiency levels:")
    for i in range(len(info['languages'])):
        print(f"\t{info['languages'][i].title()} (Proficiency: {info['proficiency'][i].title()})")