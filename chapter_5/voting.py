age = 19
if age >= 18:
    print("You are old enough to vote!")
    print ("Have you registered to vote yet?")
age = 17 
if age >= 18:
    print ("You are old enough to vote.")
    print ("Have you registered to vote yet?")
else:
    print ("\nSorry you are too young to vote.")
    print ("Please register as soon as you turn 18!")
print("\n")
age = 12
if age < 4:
    print ("Your admission cost is $0.")
elif age < 18:
    print ("Your admission cost is $5.")
else:
    print ("Your admission cost is $10.")
print("\n")
#more concise:
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >=65:
    price = 5
print("Your admission cost is $ " + str(price) + ".")


