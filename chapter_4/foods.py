my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print (my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')
print("\n")
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
print("\n")
print("\n")
for my_food in my_foods:
    print(my_food.title())
print("\n")
for friend_food in friend_foods:
    print (friend_food.title())
    