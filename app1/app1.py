# Load json data file
# working directory = C:\Users\vmp2303\Dropbox\Val_Work\Python\Training\app1
# Enter a word and return the definition from the dictionary
# If the word is not found, use difflib library to find the closest matching
# word in the dictionary, and display the definition for that word
#

import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word, data):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        response = input("Did you mean %s instead? Y/N: " % get_close_matches(word, data.keys())[0]).upper()
        if response == "Y":
            return data[get_close_matches(word, data.keys(),n=1,cutoff=0.8)[0]]
        else:
            return ("Word not found. Please double-check it")
    else:
         return ("Word not found. Please double-check it")

myword=input("Enter word: ")     

# Display the definitions on separate lines
while (myword != "q"):
    output = translate(myword, data)
    if type(output) == list:
        for x in output:
            print(x)
    else:
        print(output)
        
    myword=input("Enter word: ")  


