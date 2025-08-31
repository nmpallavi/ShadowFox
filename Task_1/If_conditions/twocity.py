city_country = {
    "mumbai": "India",
    "chennai": "India",
    "delhi": "India",
    "kolkata": "India",
    "sydney": "Australia",
    "melbourne": "Australia",
    "dubai": "UAE",
    "abu dhabi": "UAE",
    "new york": "USA",
    "los angeles": "USA",
    "london": "UK",
    "manchester": "UK"
}
city1 = input("Enter the first city: ").strip().lower()
city2 = input("Enter the second city: ").strip().lower()
if city1 in city_country and city2 in city_country:
    if city_country[city1] == city_country[city2]:
        print(f"Both cities are in {city_country[city1]}")
    else:
        print("They don't belong to the same country")
else:
    print("One or both cities are not in the database")
