def display_message (topic):
    """tell everyone what I'm learning about"""
    print ("In this chapter I'm learning about " + topic +".")

display_message('functions')

print("\n")
def display_message_2 (dog_name):
    '''tell everyone my dog's name'''
    print("My dog's name is " + dog_name.title() + ".")

display_message_2 ('lucy')

print("\n")
def message_1 (favorite_food):
    """tell everyone my favorite food"""
    print("My favorite food is " + favorite_food + ".")

message_1 ('sushi')

print("\n")
def message_2(color):
    '''let everyone know my favorite color'''
    print("My favorite color is " + color + ".")

message_2('teal')


print("\n")
def greet_user(username):
    """Display a simple greeting"""
    print("Hello, " + username.title() + "!")

greet_user("Jesse")
