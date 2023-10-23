import nltk 
#dwonload the word library 
nltk.download('wordnet')

#import WordNetLemmatizer 
from nltk.stem.wordnet import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

#problem - 1 Finding the Root of this following words  like Buses,rocks, computers,students,goes
print('#'*10+"Find the word of root"+"#"*10)
print("Rocks: ",lemmatizer.lemmatize('rocks'))
print('Students: ',lemmatizer.lemmatize('students'))
print('Goes: ',lemmatizer.lemmatize('goes'))
print('Sixers: ',lemmatizer.lemmatize('sixers'))

#problem - 2 : Lemmatize the verb with aurguments (flying -> fly, swimming -> swim)
print('\n\n')
print('*'*10+"Lemmatize Verb With Arguments"+'*'*10)
print('flying ->  ',lemmatizer.lemmatize('flying','v'))
print('swimming -> ',lemmatizer.lemmatize('swimming','v'))
print('playing -> ',lemmatizer.lemmatize('playing','v'))
print('talking -> ',lemmatizer.lemmatize('talking','v')) 

#problem - 3 : Lemmatize the adjective with arguments (good -> better -> best, tall -> taller -> tallest, small -> smaller -> smallest)
print('\n\n')
print('#'*15+"Lemmatize"+ "#"*15)
print('better -> ',lemmatizer.lemmatize('better','a'))
print('taller -> ',lemmatizer.lemmatize('taller','a'))
print('worst -> ',lemmatizer.lemmatize('worst','a'))

