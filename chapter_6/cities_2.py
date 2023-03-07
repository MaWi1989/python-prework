cities = {
    'berlin': {
        'country': 'germany',
        'population': '3,700,000',
        'fact':'used to be seperated into East and West by the Berlin Wall',
        },
    'paris': {
        'country': 'france',
        'population':'2,761,600', 
        'fact':'\' louvre museum houses the famous Mona Lisa painting',
        },
    'rome': {
        'country': 'italy',
        'population': '2;860,000',
        'fact':'has a museum entirely dedicated to pasta',
        },
    }

for city, info in cities.items():
    city = city.title()
    country = info['country']
    population = info['population']
    fact = info['fact']
    print("\n" + city + ":")
    print(city + " is located in " + country.title() + ".")
    print(city + " has a population of " + population + "." )
    print(city + " " + fact + ".")


