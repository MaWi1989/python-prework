usernames = ['John123','Bob_C','SarahConnor','Kate.Tucker.87','admin']
for username in usernames:
    if username == 'admin':
        print("Hello " + username + ", would you like to see a status report?")
    else:
        print("Hello " + username + ", thank you for logging in again!") 
print("\n")
if usernames:
     if username == 'admin':
        print("Hello " + username + ", would you like to see a status report?")
     else:
        print("Hello " + username + ", thank you for logging in again!") 
else:
    print("We need to get some users!")
         
print("\n")   
del usernames[0]
print(usernames)
del usernames[1]
del usernames[2]
print(usernames)
del usernames[0]
del usernames[0]
print (usernames)
if usernames:
     if username == 'admin':
        print("Hello " + username + ", would you like to see a status report?")
     else:
        print("Hello " + username + ", thank you for logging in again!") 
else:
    print("We need to get some users!")

print("\n")
current_users = ['Jack.Smith','car_lover123','AbbyB','janedoe','lisasimpson88']
new_users = ['jack.smith','JaneDoe','Mandy','Bob67','Matt.Smith']



for new_user in new_users:
    if new_user.lower() in current_users: 
        print ("Sorry, that username is taken. Please choose a different one.")
    else:
        print ("That username is available.")

print (current_users)
print (new_users)


        

