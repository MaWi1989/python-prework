def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("\nMy " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(animal_type='cat', pet_name='lilly')
describe_pet(pet_name='bobby', animal_type='rabbit')

print("\n")
def describe_pet(pet_name, animal_type ='dog'):
    '''Display information about a pet.'''
    print("\nI have a " + animal_type + ".")
    print("\nMy " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='willie')
describe_pet('willie')

print("\n")
describe_pet('luna')
print("\n")
describe_pet('max')

#a dog named Willie:
describe_pet(pet_name='willie')
describe_pet('willie')

#a hamster named Harry:
describe_pet('harry', animal_type='hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')
           
