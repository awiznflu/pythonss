active = True
while active:
    age= input("Eneter your age (or quit to stop)")
    if age.lower() == 'quit':
       break
    else:
        age = int(age)
        if age < 3:
            print ("Movie ticket is free")
        elif 3<= age <= 12:
            print ("It will be 10 dollars")
        else:
            print ("Movie ticket is 15 dollars")

while 1: print("This is infinite")