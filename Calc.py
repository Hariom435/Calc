# first we will take input of first number of the operation from the user.
first = input("enter first number : ")
# then we will take all the five operators so that user can choose which operation he has to conduct.
operator = input("enter operator (+,-,*,/,%) :")
# now we will take input of second number of the operation from the user.
second = input("enter second number : ")
# now for conducting operation we should have numbers. So we will convert these into integers.
first = int(first)
second = int(second)

# then again if and elif statements will come into picture.
if operator == "+":
    print(first + second)
elif operator == "-":
    print(first - second)
elif operator == "*":
    print(first * second)
elif operator == "/":
    print(first / second)
elif operator == "%":
    print(first % second)


else:
    print("Invalid operation")