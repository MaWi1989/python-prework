favorite_places = {
    'nancy': ['hawaii', 'italy'],
    'rob': ['utah', 'california', 'colorado'],
    'barb': ['paris'],
    }

for name, places in favorite_places.items():
    if len(places) > 1:
        print("\n" + name.title() + "'s favorite places are: " )
        for place in places:
            place = place.title()
            print(place)
    else: 
        print("\n" + name.title() + "'s favorite place is:")
        for place in places:
            place = place.title()
            print(place) 
