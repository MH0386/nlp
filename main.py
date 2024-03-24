# 1) get URL and get HTML from it
# 2) extract text from HTML
# 3) apply preprocessing to the text
# 4) get unique words from the text

import re

import nltk
import requests
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")

# get URL and get HTML from it
URL = "https://en.wikipedia.org/wiki/Natural_language_processing"
response = requests.get(URL, timeout=5)

html = response.text

# extract text from HTML
soup = BeautifulSoup(html, "html.parser")
paragraph = soup.find_all("p")
TEXT = [paragraph[i].text for i in range(len(paragraph))]
TEXT = " ".join(TEXT)

# cleaning
TEXT = re.sub(r"[^a-zA-Z]", " ", TEXT)

# remove whitespaces
TEXT = re.sub(r"\s+", " ", TEXT)

# convert to lower case
TEXT = TEXT.lower()

# tokenization
TEXT = word_tokenize(TEXT)

# remove stop words
TEXT = [word for word in TEXT if word not in stopwords.words("english")]

TEXT_LESS_3 = [word for word in TEXT if len(word) < 3]
# remove words with length less than 3
TEXT = [word for word in TEXT if len(word) > 2]

# Lemmatization
lemmatizer = WordNetLemmatizer()
TEXT = [lemmatizer.lemmatize(word) for word in TEXT]

# Unique words
unique_words = list(set(TEXT))
print("Unique Words", unique_words)
print()
print("Words Less Than 3", TEXT_LESS_3)
