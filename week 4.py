# name = input("What is your name?")
# print (f"\nHello, {name}")
#
# question_one = input("what is your favorite color?")
#
# print (f"{question_one} is such a pretty color")
#
# question_two = input("How old are you?")
# question_two = int(question_two)
# if question_two <= 18:
#     print (f"{question_two}, you are still young")
# else:
#     print (f"{question_two} you are old.")
#
# number = input("Enter a number and I will tell you if its even oe odd")
# number = int(number)
#
# if number % 2 == 0:
#     print (f"{number} is even")
# else:
#     print (f"{number} is odd")

# greater= input ("Give me a number")
# greater = int(greater)
#
# if greater <= 100:
#     print (f"{greater} is not greater than 100")
#
# else:
#     print (f"{greater} is greater than 100")


secret_number=44
while True:
    guess= input("Guess number between 1 and 100: ")
    guess= int(guess)
    if guess == secret_number:
        print ("You guess correctly!")
        break
    else:
        print ("Try again")