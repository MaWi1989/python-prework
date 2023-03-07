def greet_users(names):
    """Print a simple greeting for each user in the list."""
    for name in names:
        msg = (f"Hello, {name.title()}!")
        print(msg)

usernames= ['hannah', 'ty', 'margot']
print(greet_users(usernames))
