import requests
word = input("Enter a word: ")
response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
response_json = response.json()
word = response_json[0]["word"]
definition = response_json[0]["meanings"][0]["definitions"][0]["definition"]
partOfSpeech = response_json[0]["meanings"][0]["partOfSpeech"]
    
print(f"The word you entered was: {word[0].upper()+ word[1:]}")
print(f"Definition: {definition}")
print(f"This word is a {partOfSpeech}.")

