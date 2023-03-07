for value in range(1,21):
     print(value)
print ("\n")
million_numbers = list(range(1,1000001))
print (min(million_numbers))
print (max(million_numbers))
     
print("\n")
odd_numbers = list(range(1,21,2))
for odd_number in odd_numbers:
     print(odd_number)

print("\n")

threes = list(range(3,31,3))
for three in threes:
     print (three)

print("\n")
for value in range(1,6):
     print(value)
print("\n")


centuries=list(range(1600,2101,100))
for century in centuries:
     print(century)
     print(max(centuries))
print("\n")
print(centuries[0:4])
print("\n")
for century in centuries[:4]:
     print(century)
print("\n")
for value in range(1,6):
     value=value*5
     print(value)
print("\n")
tens=list(range(10,501,10))
print("\n")
print(len(tens))
print("\n")
print(tens[19:30])
print(tens)
print("\n")
for ten in tens:
     print(ten)
print(tens[:10])
print("\n")
print("\n")
cubes=[value**3 for value in range(1,11)]
print(cubes)
for cube in cubes:
     print(cube)
print("\n")
squares=[]
for value in range(1,11):
     square=value**2
     squares.append(square)
print(squares)
print("\n")
squares=[]
for value in range(1,11):
     squares.append(value**2)
print(squares)
print("\n")
print("\n")
members = ['barb','jeanne','rose','carol'] 
for member in members[:3]:
     print("Dear " + member.title() + ",\n")
     print("We're looking forward to seeing you at the next meeting!\n")
print("\n")
for member in members[3:]:
     print("Dear " + member.title() + ",\n")
     print("We were sorry to hear you can't make it to the next meeting!")
print("\n")
print("\n")
my_pet=['dog']
friend_pet=my_pet[:]
friend_pet.append('cat')
friend_pet.append('rabbit')
print(my_pet)
print("\n")
print(friend_pet)
print("\n")
foods=['pizza','tacos','dim sum','sushi']
for food in foods:
    print(f"I like to eat {food}, because they are yummy.")
    if food == 'dim sum':
        continue
print("\n")
cubes = [value**3 for value in range(1,11)]
print (cubes)

cubes = []
for value in range(1,11):
     cubes.append(value**3)
     print(cubes)
print("\n")
fives = [value*5 for value in range(1,101)]
for five in fives[19:30]:
     print(five)
