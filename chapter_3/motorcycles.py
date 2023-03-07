motorcycles = ['honda', 'yamaha', 'suzuki']
print (motorcycles)

motorcycles[0] = 'ducati'
print (motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('suzuki')
motorcycles.append('ducati')
print (motorcycles)
motorcycles.insert(1, 'yamaha')
print(motorcycles)
del motorcycles[0]
print (motorcycles)
del motorcycles[1]
print (motorcycles)
last_owned = motorcycles.pop()
print ("The last motorcycle I owned was a " + last_owned.title() + ".")
first_owned = motorcycles.pop(0)
print ("My first motorcycle was a " + first_owned.title() + ".")
motorcycles = ['ducati', 'honda', 'yamaha']
print (motorcycles)
motorcycles.remove('ducati')
print (motorcycles)
motorcycles.append('ducati')
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print (motorcycles)
print ("\nA " + too_expensive.title() + "is too expensive for me." )


