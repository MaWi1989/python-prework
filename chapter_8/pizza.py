def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers' , 'extra cheese')

print("\n")
def make_pizza(*toppings):
    """Summerize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings: ")
    for topping in toppings:
        print("- " + topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers' , 'extra cheese')


print("\n")
def make_pizza(size, *toppings):
    """Summerize the pizza we are about to make."""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings: ")
    for topping in toppings:
        print("- " + topping)

