dream_vacations = {}

polling_active = True

while polling_active:
    
    name = input("\nWhat is your name? ")
    destination = input("\nIf you could go anywhere in the world, where would you go? ")

    dream_vacations[name] = destination
    
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("...Poll Results:...")
for name, destination in dream_vacations.items():
    name = name.title()
    destination = destination.title()
    print(name + " would love to go to " + destination + ".")
