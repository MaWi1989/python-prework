person_1 = {
    'first': 'ingrid',
    'last': 'fiebig',
    'age': 71,
    'city': 'berlin',
    }
print("The person's first name is " + person_1['first'].title() + ".")
print("The person's last name is " + person_1['last'].title() + ".")
print("The person's age is " + str(person_1['age']) + ".")
print("The person lives in " + person_1['city'].title() + ".")

print("\n")
person_2 = {
    'first': 'mareen',
    'last': 'bayer',
    'age': 34,
    'location': 'milwaukee',
    }

person_3 = {
    'first': 'anne',
    'last': 'marth',
    'age': 33,
    'location': 'munich',
    }

people = [person_1, person_2, person_3]

# for key, value in people.items():
#     print("This person's name is ")
#     full_name = value['first'] + " " + value['last']
#     age = value['age']
#     location = value['location']
#     print( "/nThis person's name is " + full_name + ".")


for person in people:
    full_name = person['first'] + " " + person['last']
    age = person['age']
    location = person['location']

    print("Name: " + full_name)
    print("age: " + age)
    print("location: " + location)