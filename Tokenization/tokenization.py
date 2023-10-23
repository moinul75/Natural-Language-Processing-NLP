"""
NLTK Text Normalization 
Topic: Token Authentication 
Exersices are included by 
index : 
  1. Sentenece Tokenize 
  2. work Tokenize 
  3. white space tokenize 
  4. word punct Tokenize 
  5. Frequency Distribution 
  6. plot Frequency Distribution (Cumolative True/False) (Using mathplotlib)
"""

import nltk 
nltk.download('punkt')
from nltk.tokenize import sent_tokenize,word_tokenize,wordpunct_tokenize,WhitespaceTokenizer 




sentence = "The objectives of software engineering encompass various goals and principles that guide the development, maintenance, and management of software systems. These objectives are designed to ensure that software is reliable, maintainable, and meets the needs of its users. Here are some of the key objectives of software engineering:"

token = sent_tokenize(sentence)
# print(token)


#word tokenization 
word = word_tokenize(sentence)
# print(word)

#wordpunct tokenize 
word_punc = wordpunct_tokenize(sentence)
# print(word_punc)

#white space tokenize 
white_space = WhitespaceTokenizer().tokenize(sentence)
# print(white_space)

#now count the frequency of this sentence 
from nltk.probability import FreqDist 

frequent = FreqDist(word)

common_word = frequent.most_common()
print(common_word)


#show the frequency plot 
import matplotlib.pyplot as plt
plts = frequent.plot(30,cumulative=False)
cum = frequent.plot(30,cumulative=True)
print(cum)
print(plts)

