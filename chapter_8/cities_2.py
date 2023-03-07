def describe_city(name, country='germany'):
    """Tell a city and it's country"""
    print("\n" + name.title() + " is in " + country.title() + ".")

describe_city('berlin')
describe_city('frankfurt')
describe_city('paris', country='france')
