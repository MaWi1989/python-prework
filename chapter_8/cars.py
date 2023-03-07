def make_car(manufacturer, model, **car_info):
    """Return a dictionary about all the information of a car."""
    car = {}
    car['make'] = manufacturer
    car['model'] = model 
    for key, value in  car_info.items():
        car[key] = value 
    return car

made_car = make_car('subaru', 'legacy', year= 2014, color= 'black')
print(made_car)

