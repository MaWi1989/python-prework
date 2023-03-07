favorite_number = {
    'john': [2,4,6],
    'peter': [6,13],
    'mary' : [8,17],
    'jim': [7,65,100],
    'lisa': [8,10],
    }

for name, numbers in favorite_number.items():
    print(name.title() + "'s favorite numbers are " + str(numbers) + ".")
