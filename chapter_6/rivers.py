rivers = {'seine': 'france', 'nile': 'egypt', 'amazon':'peru',}
for river, country in rivers.items():
    print("The " + river.title() + " runs through " + country.title() + ".\n")
for river in rivers.keys():
    print(river.title())
print("\n")
for country in rivers.values():
    print(country.title())
