# dictionaries
user = {
    "name": "Dedrick",
    "lastName": "Crudup",
    "age": 24,
}
print(user)
print(type(user))
print(user["name"] + " " + user["lastName"])

# array but in Python, this is a list
numbers = [1, 2, 3]  # Rename variable to "numbers" for clarity
print(numbers)
numbers.append(4)
print(numbers)

print(len(numbers))#count items
print(len(user["name"]))#count characters
print(len(user))

ages = [32, 74, 20, 69, 52, 26, 31, 77, 43, 73, 51, 57, 19, 79, 40, 34, 27, 23, 21, 44, 53, 55, 24, 36, 41, 47, 78, 46, 68, 75, 49, 83, 61, 60, 29, 56, 67, 17, 70, 81, 87, 38]

def exc1():
    #print all the numbers in ages
    #calculate the ttal sum of the numbers in age
    # count how manynames in ages are less than 30
    total = 0
    count = 0
    total += age
    for age in ages:
        print(age)
        if age <30 and age < 50:
            count += 1
    print(total)
    print("There are "+str(count)+ "numbers between 30 and 50")
        #call the function
exc1()
    