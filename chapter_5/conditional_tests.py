name = 'bob'
print("Is name == 'bob'? I predict True.")
print( name == 'bob')
print("\nIs name == 'bill'? I predict False.")
print( name == 'bill')
print("\n")
#1
animal = 'dog'
print("Is animal == 'dog'? I predict True.")
print (animal == 'dog')

#2
song = 'complicated'
print("\nIs song == 'complicated'? I predict True.")
print(song == 'complicated')

#3
letter = 'm'
print ("\nIs letter == 'm'? I predict True.")
print (letter == 'm')

#4
number = 8
print("\nIs number == 8? I predict True.")
print(number == 8)

#5
age = 25 
print("\nIs age == 25? I predict True.")
print (age == 25)

#6
actor = 'tom cruise'
print ("\nIs actor == 'brad pitt'? I predict False.")
print (actor == 'brad pitt')

#7
color = 'blue'
print("\nIs color == 'green'? I predict False.")
print(color == 'green')

#8 
sign = 'virgo'
print ("\nIs sign == 'pisces'? I predict False.")
print(sign == 'pisces')


shape = 'triangle'
print ("\nIs shape == 'square'? I predict False.")
print (shape == 'square')

#10
drink = 'coke'
print ("\nIs drink == 'sprite'? I predict False.")
print (drink == 'sprite')
print("\n")
food = 'sushi'
if food == 'sushi':
    print ("I really like " + food + ".")
if food != 'sushi':
    print("I don't like " + food + "as much as I like sushi.")
print("\n")
color = 'green'
if color != 'red':
    print("The color " + color + " would be great for my bedroom walls.")
print("\n")
name = 'John'
print(name == 'john')
print(name.lower() == 'john')
print("\n")

group = 32

if group >= 20:
    print ("Good morning, guy's!")
    print ("Are you ready for our trip?")
if group < 20:
    print ("Good morning, guys!")
    print 
    ("unfortunately, there are only " 
     + group + " people here today, so we have to cancel the trip.")
print("\n")

group = 12

if group >= 20:
    print ("Good morning, guy's!")
    print ("Are you ready for our trip?")
if group < 20:
    print ("Good morning, guys!")
    print ("Unfortunately, there are only " 
     + str(group) + " people here today, so we have to cancel the trip.")
print("\n")
riders = 15
if riders <= 4:
    print ("car")
elif riders <= 8:
    print ("van")
else:
    print ("bus")
print("\n")
age = 5
print (age == 5)
print (age != 10)
print (age == 8)
print("\n")
time_1 = '7:00'
time_2 = '8:00'
if time_1 or time_2 == '7:00':
    print ("Time to wake up!")
print("\n")
riders_1 = 2
riders_2 = 3
print(riders_1 <= 4 and riders_2 <= 4)
print("\n")
likes = ['apples', 'strawberries','pears']
fruit = 'bananas'
print(fruit in likes)
if fruit in likes:
    print("Buy " + fruit +".")
if fruit not in likes:
    print ("\nDo not buy " + fruit +".")
print (fruit not in likes)
print (fruit in likes)








