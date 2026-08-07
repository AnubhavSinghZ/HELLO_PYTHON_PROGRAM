#1
alien_0={"color": "green", "points": 5}
alien_1={"color": "yellow", "points":10}
alien_2={"color": "red", "points": 15}
# Making a list of dictionaries

aliens=[alien_0,alien_1, alien_2]
for alien in aliens:
    print(alien)


#2
#Make an empty list for storing monkeys

monkeys=[]

#Make 30 green monkeys
for monkey_number in range(30):
    new_monkeys={'color': "green", "points": 5, "speed": "slow"}
    monkeys.append(new_monkeys)
for monkey in monkeys[:3]:
    if monkey['color']=="green":
        monkey["color"]='yellow'
        monkey["speed"]= "medium"
        monkey['points']=10        


# Show the first 5 monkeys
for monkey in monkeys[:5]:
    print(monkey)
print("--")
print(f"Total number of monkeys:{len(monkeys)}")