requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")
print("\n")
requested_toppings = ['mushrooms', 'onions','pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)
print("\n")

#test multiple conditions:
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Add pepperoni.")
if 'extra cheese' in requested_toppings:
    print ("Adding extra cheese.")
print("\nFinished making your pizza!")
print("\n")
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print ("Adding " + requested_topping + ".")
print ("\nFinished making your pizza!")
#out of green peppers:
print("\n")
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print ("Sorry we are out of green peppers right now.")
    else:
        print ("Adding " + requested_topping + ".")
print ("\nFinished making your pizza!")
print("\n")
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print ("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print ("Are you sure you want a plain pizza?")
    




