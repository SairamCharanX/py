#Program to convert JSON file into a python dictionary

import json

#Opening the JSON file
initPointer = open('sample.json')

#Loading the file contents into a dictionary
containerDictionary = json.load(initPointer)

#printing the dictionary
print(containerDictionary)


