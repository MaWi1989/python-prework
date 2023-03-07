# 3-4 Guest List
guests = ['Taylor Swift', 'Sandra Bullock', 'Channing Tatum' ]
message_1 = "Dear " + guests[0].upper() + ", would you please come over for Dinner Saturday night?"
message_2 = "Dear " + guests[1].upper() + ", would you like to come for dinner?"
message_3 = "Dear " + guests[2].upper() + ", do you want to come over for dinner some time?"
print (message_1)
print (message_2)
print (message_3)

print (guests)
print ("\nUnfortunately, " + guests[-1] + " cannot make it tonight.")
guests.remove('Channing Tatum')
print (guests)
guests.append('Christina Aguilera')
print (guests)  
message_4 = ("Dear " + guests[0].upper() + ", please come over next week instead. Thank you!")
message_5 = ("Dear " + guests[1].upper() + ", we had to reschedule dinner until next week.")
message_6 = ("Dear " + guests[2].upper() + ", I would love it if you could join me for dinner next weekend!" )
print (message_4)
print (message_5)
print (message_6)

print(guests)
print ("\nGood news, guys, I found a bigger table, so we can have more people for dinner!")
guests.insert(0, 'Avril Lavigne')
guests.insert(3,'Ed Sheeran')
guests.append('Shawn Mendes')
print (guests)

message_7 = "Dear " + guests[0] + ", please come to dinner!"
message_8 = "Dear " + guests[1] + ", please come to dinner!"
message_9 = "Dear " + guests[2] + ", please come to dinner!"
message_10 = "Dear " + guests[3] + ", please come to dinner!"
message_11 = "Dear " + guests[4] + ", please come to dinner!"
message_12 = "Dear " + guests[5] + ", please come to dinner!"
print (message_7)
print (message_8)
print (message_9)
print(message_10)
print (message_11)
print (message_12)
print (len(guests))
print ("I have invited 6 of you to dinner.")
print ("I have invited " + str(len(guests)) + " of you to dinner.")

print (guests)
print ("\nUnfortunately, guys, my new table won't arrive in time for our dinner. That means I only have room to invite 2 poeple.")
uninvite_1 = guests.pop(5)
print ("\nDear " + uninvite_1 + ", I'm sorry, but I can't invite you to dinner after all.")
uninvite_2 = guests.pop(4)
print ("\nDear " + uninvite_2 + ", I'm sorry, but I can't invite you to dinner after all.")
uninvite_3 = guests.pop(3)
print ("\nDear " + uninvite_3 +", I'm sorry, but I can't invite you to dinner after all.")
uninvite_4 = guests.pop(2)
print ("\nDear " + uninvite_4 + ", I'm sorry, but I can't invite you to dinner after all.")
print (guests)
print ("\nDear " + guests[0] + ", you are still invited to dinner.")
print ("\nDear " + guests[1] + ", you are still invited to dinner.")
print(guests)
del guests[0]
print (guests)
del guests[0]
print (guests)
print (len(guests))


 