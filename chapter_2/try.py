message = "Hi!"
print (message)
message = "I'm new here."
print (message)
message = "My name is Manja."
print (message)

name = ' boy '
print (name)
print (name.strip())
print (name.rstrip())
print (name.lstrip())
name = " boy "
print (name)
print (name.strip())
print (name.rstrip())
print (name.lstrip())

print (name + ",come over here")
message = ", come over here"
print (name, message)
print (message)

names = ['gary', 'manja', 'hailey', 'lucy']
print (names[1].title())
print (names[2].title())
print (names[1] + " " + names[2])

print (names[1])
print (names[2])
 
letters = ['a', 'b', 'c', 'd'] 
print (letters)
letters[1] = 'a'
print (letters)
letters.append('e')
print (letters)
letter = letters.pop()
print ("Elephant starts with an " + letter + ".")
print ("Apple starts with an " + letters.pop(0) + ".")
del letters[-1]
print (letters)

letters_2 = []
print (letters_2)
print ("\n")       
print ("\n")
greeting = 'Hello, hello, hellooo,'
name = 'Jimmy'
print (greeting + " " + name +"!")
print (greeting , name, sep= " ")
print ("\n")
print (type(name))
print ("\n")
print(name.title())
print(greeting)
print(greeting , name , sep= " ")
print("\tHello")
