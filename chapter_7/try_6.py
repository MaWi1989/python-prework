responses = {}

polling_active = True

while polling_active:
    
    name = input("\nWhat is your name? ")
    response = input("\nWhat mountain would you like to climb someday? ")

    responses[name] = response 
    
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("---Poll Results---")
for name, response in responses.items():
    name = name.title()
    response = response.title()
    print(name + " would like to climb " + response + ".")



