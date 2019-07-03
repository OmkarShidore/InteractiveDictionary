#import libs
import json
from difflib import get_close_matches

#load json dict
data=json.load(open('data.json'))

def translate(w):
    w=w.lower()
    if w in data:
        return data[w]
    if len(get_close_matches(w,data.keys()))>0:
           response=input("Did you mean: '%s' [Y/N]:"  %get_close_matches(w,data.keys())[0])
           if response=='y' or response=='Y' or response=='yes' or response=='Yes' or response=='YES':
               return data[get_close_matches(w,data.keys())[0]]
           else:
               return "This Word doesn't exist."
    else:
           return "This word dosen't exist."

#main
word=input("Please Enter a word: ")
result=translate(word)
print(result)