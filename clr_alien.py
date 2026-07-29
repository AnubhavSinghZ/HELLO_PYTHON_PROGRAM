alien_0={'x_position':0, 'y_position':25, "speed":"medium"}
print(f"Original Postion:{alien_0['x_position']}")

#MOVE THE ALIEN TO THE RIGHT

if alien_0['speed']== 'slow':
    x_increment =1
elif alien_0['speed']== 'medium':
    x_increment =2
else:
    # This  must be a fast alien.
    x_increment=3

#The new position of alien
alien_0['x_position']=alien_0['x_position']+x_increment

print(f"New Position: {alien_0['x_position']}")