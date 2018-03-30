print("\nPrinting alien_0 dictionary.")
alien_0 = {'color':'green','points':5}
print(alien_0)

print("\nAdding screen position to dictionary.")
print("x_position = 0")
alien_0['x_position'] = 0
print("y_position = 25")
alien_0['y_position'] = 25

print("\nPrinting new dictionary contents.")
print(alien_0)

print("\nYou shot an alien")
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!\n")

print("\nDeleting points key-value pair from dictionary.")
del alien_0['points']
print("\nPrinting new dictionary contents.")
print(alien_0)


