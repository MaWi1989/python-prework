current_users = ['Jack.Smith','car_lover123','AbbyB','janedoe','lisasimpson88']
new_users = ['jack.smith','JaneDoe','Mandy','Bob67','Matt.Smith']

for new_user in new_users:
    if new_user.lower() in current_users: 
        print ("Sorry, that username is taken. Please choose a different one.")
    else:
        print ("That username is available.")

print (current_users)
print (new_users)