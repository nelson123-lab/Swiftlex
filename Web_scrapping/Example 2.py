import requests
from bs4 import BeautifulSoup

# the word to look up
word = "example"

# send a GET request to Google search
google_url = f"https://www.google.com/search?q={word}+meaning"
response = requests.get(google_url)

# parse the search results page and find the link to the dictionary website
soup = BeautifulSoup(response.content, "html.parser")
dictionary_link = soup.find("a", href=True, text="dictionary.com")["href"]

# send a GET request to the dictionary website
response = requests.get(dictionary_link)

# parse the dictionary page and find the element containing the word's meaning
soup = BeautifulSoup(response.content, "html.parser")
meaning_element = soup.find("div", {"class": "default-content"})

# extract the word's meaning and pronunciation audio file
meaning = meaning_element.find("span", {"class": "one-click-content"}).text
audio_file = meaning_element.find("audio")["src"]

# store the data in a dictionary
word_meaning = {word: meaning}

# save the audio file
response = requests.get(audio_file)
with open(f"{word}.mp3", "wb") as f:
    f.write(response.content)
