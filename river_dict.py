rivers ={
    "nile": "egypt",
    "ganga": "india",
    "amazon": "america"
}
# to print the key and values together
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

# for the key only (River name)   
for river in rivers.keys():
    print(f"{river.title()}")

# for the values only (Country Name)
for country in rivers.values():
    print(f"{country.title()}")