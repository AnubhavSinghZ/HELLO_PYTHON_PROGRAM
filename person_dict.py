#The details of a person

person={
    "first_name": "XYZ",
    "last_name": "ABC",
    "age": 20,
    "city": "ABCXYz"
}
print(f"The Person Details: {person}")

#Favorite Number
fav_num={
    "Prince":10,
    "Anubav":7,
    "Abhishek":18,
    "Aman":45
 }
for name, number in fav_num.items():
    print(f"{name}'s favorite number is {number}.")

# Polling from friends for data
fav_num
num_friends=int(input("How many friends are you polling?"))
for i in range(num_friends):
    name=input(f"\nEnter name for friend {i+1}").strip().title()
    num=int(input(f"Enter {name}'s fav number"))
    fav_num[name]=number
print("\n___Poll Result___")
for name, number in fav_num.items():
    print(f"{name}'s fav number is {num}")