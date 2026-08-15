# Create a list containing different pets

pets = ['dog', 'lion', 'cat', 'cow', 'crow', 'cat']

print(pets)
# Keep looping as long as 'cat' is present in the list
while 'cat' in pets:
# Remove one occurrence of 'cat' from the list
    pets.remove('cat')

print(pets)