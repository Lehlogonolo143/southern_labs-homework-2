# Author: SE Class

"""
This greets the user and welcomes them :
:return: None
"""
def greet_user():
    print("Hello, Engineers") 
    print("Welcome to session 4!")

greet_user()

def student_info(full_name):
    full_name = input("please enter your name: ")
    print("Hello" , full_name)
    
student_info("Pontsho")

def say_hello(name):
    print("Hello" ,name)
    print("How are you" ,name)

say_hello("Ídah")

def sum_numbers(x):
    return 3 * x

numbers = sum_numbers(5)
print(numbers)

def divide_numbers(x):
    return x / 2
div_numbers = divide_numbers(8)
print(div_numbers)

