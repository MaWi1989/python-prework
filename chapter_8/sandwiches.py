def sandwiches(*toppings):
    """Summarize the sandwich order with all the toppings."""
    print("Making a sandwich whith the following toppings: ")
    for topping in toppings:
        print("- " + topping)

sandwiches('ham', 'american cheese', 'mayo')
sandwiches('tuna salad', 'lettuce')
sandwiches('turkey breast', 'cheddar cheese', 'mayo', 'lettuce')
