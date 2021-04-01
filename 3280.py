from bs4 import BeautifulSoup
import requests

url = "https://tools.ietf.org/html/rfc3280"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
words = soup.text.split()
nine_letter_words = [w for w in words if len(w) == 9]
most_frequent_word = max(set(nine_letter_words), key = nine_letter_words.count)
print(most_frequent_word)
