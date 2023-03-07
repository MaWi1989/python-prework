name = input("Please enter your name: ")
print("Hello, " + name + "!")

prompt = "If you tell us who you are we can personalize the messages you see."
prompt += "What is your first name? "

name = input(prompt)
print("\nHello, " + name + "!")

print("\n")

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(Enter 'q' at any time to quit)")
    
    f_name = input("First name:")
    if f_name == 'q':
        break

    l_name = input("Last name:")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("Hello " + formatted_name + "!")


