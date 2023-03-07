responses = {}

#set flag to indicate poll isnactive:
polling_active = True

while polling_active:
    
#promt for person's name and response:
    name = input("\nWhat is your name? ")
    response = input("\nWhat mountain would you like to climb someday? ")


#store response in dictionary:
    responses[name] = response 
    

#anyone else taking this poll?:
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

#polling complete, show results:
print("---Poll Results---")
for name, response in responses.items():
    print(name.title() + " would like to climb " + response + ".")



