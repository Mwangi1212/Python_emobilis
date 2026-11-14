# store many items
ages = [21, 72, 43, 76, 23, 78, 88, 90, 15]  # list

names = ["Zack", "Jane", "Jack", "Moha", "Rick", "Jack"]  # 10 9
# functions
ages.append(100)  # add item to the end of the list
ages.sort()  # sort the list in ascending order
ages.reverse()  # reverse the order of the list
print(ages)

# names.sort()  # sort the list in ascending order
print(names)

names.count("Jack")  # count the number of occurrences of "Jack" in the list    

jack_count = names.count("Jack")
print(jack_count)  # print the count of "Jack"

print(len(names))  # print the length of the list
print(len(ages))  # print the length of the list

print(sum(ages)/len(ages))  # print the sum of the ages

# retrieve an element
print(names[0])

print(names[-1])   #python allows negative indexing to retrieve elements from the end of the list

print(names[-2])  # retrieve the second last element

print(names[-3:])  # retrieve the last three elements of the list #slicing


print(ages[2:5])  # retrieve elements from index 2 to 4 (5 is exclusive)

print(ages[:2])  # retrieve every second element from the list

# set
# names={"Zack", "Jane", "Jack", "Moha", "Rick", "Jack"}  # set
scores = {90, 80,80,70, 60, 50, 40, 30, 20, 10}  # set
print(scores)  # print the set (duplicates are removed)
scores.add(100)  # add an item to the set
scores.remove(20)  # remove an item from the set

# tuple
weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")  # tuple
print(weekdays)  # print the tuple

# dictionary
student = {"name": "Zack", "age": 21, "gender": "male"}  # dictionary
print(student)  # print the dictionary
print(student["name"])  # retrieve the value associated with the key "name"

people=[{"name":"Lexy","age":"21"},
         {"name":"Zack","age":"20"},
         {"name":"Jane","age":"22"}
        ]
print(people[0]["name"])  # print the list of dictionaries

# loops

