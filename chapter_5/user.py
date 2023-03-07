user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

for key, value in user_0.items():
    if key!= 'username':
        print("\nKey: " + key.title())
        print("Value: " + value.title())
    else:
        print("\nKey: " + key)
        print("Value: " + value)
