# function methods
from custom_functions import greet  # import the function from the custom_functions.py file

print("Hello World")  # print a string

with open("hello.txt", "w") as f:
    f.write("Hello World\n")  # write a string to a file
    f.write("Caroline Mwangi\n")  # write a string to a file
    f.write("Emobilis\n")  # write a string to a file

with open("hello.txt", "r") as f:
    content = f.read()  # read the content of the file
    print(content)  # print the content of the file

    # pip install yt-dlp

greet()  # Call the function to execute it