def greet():
    print("Hello, welcome to the program!")

# greet()  # Call the function to execute it

def greeting(name):
    print(f"Hello, {name}! Welcome to the program!")

def volume_cylinder(radius, height):
    pi = 3.14159
    volume = pi * radius ** 2 * height
    print(f"The volume of the cylinder is: {volume}")

def volume_cylinder2 (radius,height):
    pi = 3.14159
    volume = pi * radius ** 2 * height
    return volume

def volume_surface(radius, height):
    v = 22 / 7 * radius**2 * height
    a = 22/7 * radius**2 *2 + 22/7 * radius* 2 *height
    return v, a

# volume_cylinder(height=5, radius=10)
# volume_cylinder(radius=10, height=20)

volume, area= volume_surface(radius=10, height=20)
print(f"Volume is {volume} and Area is {area}")

# named parameters allow you to specify the values of the parameters by name, rather than by position. This can make your code more readable and easier to understand, especially when a function has many parameters.
#named parameters
v, a = volume_surface(height=20, radius=10)
print(f"Volume is {v} and area is {a}")


def divide(a, b, should_round=False):
    res= a / b
    if should_round== True:
        return round(res,2)
    else:
        return res

print(divide(9, 5.11,True))

print(divide(8, 11))