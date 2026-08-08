# Practice of Dicionary with List

pizza={
    'crust': "thick",
    "toppings": ['mushroom', 'extra cheese'],
    }
print(f"You ordered a {pizza['crust']}- crust pizza wit the following toppings")
for topping in pizza['toppings']:
    print(f'\t{topping}')