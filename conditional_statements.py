import os

import sys

name=input("Enter your name:")

age=input("Enter the age:")

if not age.isnumeric():
    print("Invalid age")
    # teminate
    os._exit(0)

if int(age) >18:
    print(name, "is an adult")
else:
    print(name, "is a minor")