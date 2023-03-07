def build_dog(name, color, breed, age=''):
    """Return a dictionary of information about a dog."""
    dog = {'dog_name':name, 'dog_color':color, 'dog_breed':breed}

    if age:
        dog['age'] = age 

    return dog

my_dog = build_dog('lucy', 'white', 'american bulldog', age= 2)
print(my_dog)

my_dog = build_dog('piper', 'black', 'labrador', age= 3)
print(my_dog)

my_dog = build_dog('pumpkin', 'tan', 'chihuahua')
print(my_dog)