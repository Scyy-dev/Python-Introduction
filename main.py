# Project 1
print("Hello, world!")

# Project 2
# This project fails because we need to add a float() around the inputs!
num1 = input("Enter a number: ")
num2 = input("Enter a number: ")
result = num1 + num2
print(result)

num1 = float(input("Enter a number: "))
num2 = float(input("Enter a number: "))
result = num1 + num2
print("Result:", result)

# Project 3
age = 17
if age >= 18:
    print("Welcome to the club")
else:
    print("You're too young!")

# Project 4
for countdown in range(10, 1, -1):
    print(str(countdown) + "!")
print("Liftoff!")

countdown = 10
while countdown > 0:
    print(str(countdown) + "!")

# Project 5
while True:
    direction = input("Enter a direction [N/E/S/W]: ")
    if direction == "N":
        print("You fall into a trap and died! Try again!")
    elif direction == "E":
        print("You get lost in a forest! Try again!")
    elif direction == "S":
        print("You found the treasure! Congrats!")
        break
    elif direction == "W":
        print("You run into a band of angry goblins who rob you! Try again!")
    else:
        print("Unknown direction!")

# Project 6
"""
Same as project 5, but they can traverse the following map:

S###T
 
Key:
S - start
# - movable space
T - treasure (end) 
"""
