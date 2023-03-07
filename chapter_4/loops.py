pizzas = ['cheese', 'pepperoni', 'hawaii', 'veggie']
for pizza in pizzas:
     print (pizza)
     print ("I like " + pizza.title() + " pizza.\n")
print ("My favorite pizza is " + pizzas[2].title() + ".")
print ("\n")
print ("\n")
friend_pizzas = pizzas[:]
pizzas.append('mushroom')
friend_pizzas.append('sicilian')
print("My favorite pizzas are:")
for pizza in pizzas:
     print(pizza.title())
print("\nMy friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
     print(friend_pizza.title())
print("\n")
print("\n")


animals = ['dog', 'cat', 'bird']
for animal in animals:
     print(animal)
     print ("A " + animal + " would make a great pet.")

print ("\nAll of these animals would make a great pet!")

print ("\n")
print ("\n")
recipients = ['mom', 'dad', 'viola', 'marco']
for recipient in recipients:
     print ("Dear " + recipient.title() + ",\nWe wish you a merry Christmas.\n")
print ("\nHappy Holidays, everyone!")