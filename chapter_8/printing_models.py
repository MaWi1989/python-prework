unprinted_designs = ['phone case', 'robot', 'dog']
completed_models = []
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print("Printing model: " + current_design)
    completed_models.append(current_design)

print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

print("\n")

def print_models(unprinted_designs, completeed_models):
    """Simulate printing each model until none are left.
    Move each design to completed_models after printing."""
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed.")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot', 'dog']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
