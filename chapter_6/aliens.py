alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

alien_0 = {'color':'green'}
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'])

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))

#move the alien to the right
#determine how far to move the alien based on current speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

#new position is old position + increment
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

del alien_0['speed']
print("\n")
print(alien_0)
print("\n")
alien_0 = {}
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

#make an empty list for storing aliens:
aliens = []

#make 30 aliens:
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

#show first 5:
for alien in aliens[:5]:
    print(alien)
print("...")

#show how many aliens have been created:
print("Total number of aliens: " + str(len(aliens)))
print("\n")
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow',
        alien['speed'] = 'medium',
        alien['points'] = 10

for alien in aliens[:5]:
    print(alien)
print("...")

