# Functions with input
from itertools import count


# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
#
# greet_with_name("Jack Bauer")

def greet_with(name,age):
    print(f"Your name is {name}")
    print(f"Your age is {age}")

greet_with("chanbin",20)
greet_with(age=20, name="chanbin")

