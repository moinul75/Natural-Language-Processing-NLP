import nltk 
nltk.download('punkt')
from nltk.collections import Counter 
from nltk.tokenize import word_tokenize

#now use String CaseFold use to make all the string in a lower()
text = "Natural Language Toolkit (NLTK) is a comprehensive Python library for working with human language data. It is a powerful tool for natural language processing (NLP) and text analysis tasks. NLTK provides easy-to-use interfaces and resources for accomplishing a wide range of NLP tasks. Here's an overview of NLTK's key features and capabilities:"

caseFold = text.casefold()
# print(caseFold)

#to_lower()
caseFolds = text.lower()
# print(caseFolds)

#Using nltk to do the similar form of action and count all the words with word_tokanize 
words = word_tokenize(text)

#make this all words ar in smaller 
wrd = [word.lower() for word in words]

print(wrd)

count = Counter(wrd)
print(count)