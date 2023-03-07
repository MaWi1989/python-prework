sandwich_orders = ['pastrami', 'ham&cheese', 'italian', 'pastrami', 'tuna', 'pastrami']
finished_sandwiches = []
print(sandwich_orders)

print("\nSorry, the Deli has run out of Pastrami!")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)
print("\n")

while sandwich_orders:
    made = sandwich_orders.pop()
    print("I made your " + made + " sandwich.")
    finished_sandwiches.append(made)

else: 
    print("\nSandwiches made: ")
    for finished_sandwich in finished_sandwiches:
        print(finished_sandwich)


