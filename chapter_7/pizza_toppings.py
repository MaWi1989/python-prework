prompt = "\nPlease enter a pizza topping you would like: "
prompt += "\nEnter 'quit' when done. "

while True:
        topping = input(prompt)
        if topping == 'quit':
                print("Your pizza is done.")
                break 

        else: 
                print("Adding " + topping + " to your pizza.")

