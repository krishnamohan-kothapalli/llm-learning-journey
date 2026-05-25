# Create a dictionary called car with the keys "brand", "model", "year" and values "Ford", "Mustang", 2024
# Print the value of the "model" key
# Add a new key "color" with the value "red"
# Remove the "brand" key using pop()
# Print the dictionary

thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 2024
}

print(thisDict)

print(thisDict["model"])
thisDict["color"] = "red"

thisDict.pop("brand")
print(thisDict)