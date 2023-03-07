def city_country(city,country):
    """List name of a city and the countre it's in."""
    result = city + ", " + country
    return result.title()

place = city_country('berlin', 'germany')
print(place)

place = city_country('london', 'england')
print(place)

place = city_country('paris', 'france')
print(place)