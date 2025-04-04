# Hot Beverage Program

def showMenu():
    print("Welcome to the Beverage Shop!")
    print("1. Coffee - $1.00")
    print("2. Tea - $0.75")
    print("3. Hot Chocolate - $1.25")
    print("4. Cappuccino - $2.50")
    print("5. Quit")
    beverage = int(input("Please choose a beverage of your choosing (1-5): "))
    return beverage


def calcCost(beverageOrder):
    cost = 0.00
    for item in beverageOrder:
        # Item # 1 Coffee $1.00
        if item == 1:
            cost += 1.00
        # Item # 2 Tea $0.75
        elif item == 2:
            cost += 0.75
        # Item # 3 Hot Chocolate $1.25
        elif item == 3:
            cost += 1.25
        # Item # 4 Cappuccino $2.50
        elif item == 4:
            cost += 2.50
    print(f"The total cost is $ {cost:.2f}")


def main():
    beverageOrder = []

    while True:
        beverage = showMenu()

        if beverage == 5:
            print("Thank you for visiting! Come back again soon! Goodbye.")
            break

        if beverage in [1, 2, 3, 4]:
            beverageOrder.append(beverage)
            print(f"Your order currently is: {beverageOrder}")
        else:
            print("Invalid choice, please select a valid option.")

    # Calculate the total cost after the loop ends
    calcCost(beverageOrder)


main()
