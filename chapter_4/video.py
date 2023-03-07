foods=['pizza','tacos','dim sum','sushi']
print(foods[1])
for food in foods:
    print(f"I like to eat", food.title())
    print(type(food))
print("loop is over")
print("\n")
for food in foods:
    print(f"I like to eat {food}, because they are yummy.")
    if food == 'dim sum':
        break
print("\n")
for food in foods:
    if food == 'dim sum':
        continue
    print(f"I like to eat {food}, because they are yummy.")
print("\n")
for index in range(len(foods)):
    print (index)
print("\n")
for index in range(len(foods)):
    print(index)
    print(foods[index])
    print("\n")
print(list(enumerate(foods)))
for tup in enumerate(foods):
    print(tup)
print("\n")
for index,food in enumerate(foods):
    print(f"My number {index+1} food is {food.title()}.")

    