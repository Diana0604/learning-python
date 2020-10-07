## Welcome to the calculator manager! You DO NOT need to modify this file
import calculator

user = input("What's your name? ")

calculator.greet(user)

while(True):
    action = input("Do you want to sum, substract, multiply or divide? ")
    a = int(input("What is the first number of your " + action + "? "))
    b = int(input("What is the second number of your " + action + "? "))
    if(action == "sum"):
        print(calculator.sum(a,b))
    if(action == "substract"):
        print(calculator.substract(a,b))
    if(action == "divide"):
        print(calculator.divide(a,b))
    if(action == "multiply"):
        print(calculator.multiply(a,b))