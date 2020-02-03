from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("notebook"))
print(lemmatizer.lemmatize("book"))
print(lemmatizer.lemmatize("books"))
print(lemmatizer.lemmatize("library"))
print(lemmatizer.lemmatize("libraries"))
