pets= {
    'max': {
        'animal': 'dog',
        'owner': 'john',
        },

    'lilly': {
        'animal': 'cat',
        'owner': 'sarah',
        },
    }



for pet in pets:
    print(pet)

for fact, info in pets.items():
    print(fact)
    print (info)
print("\n")




for pet in pets:
    for fact, info in pets.items():
        print("\n" + pet.title() + " is a " + info['animal']  + 
              " who belongs to " + info['owner'].title() + ".")

        