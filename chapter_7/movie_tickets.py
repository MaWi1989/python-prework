prompt = "If you tell me your age I will tell you your ticket cost. "
prompt += "What is your age? "

age = input(prompt)
age = int(age) 

if age < 3: 
    print("Your ticket is free.")
elif age < 13:
    print("Your ticket costs $10.")
else:
    print("Your ticket costs $15.")
    