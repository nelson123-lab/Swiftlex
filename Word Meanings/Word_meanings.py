from PyDictionary import PyDictionary
# Meaning of Word using dictionary1
dictionary1 = PyDictionary()
# Meaning of Words in Dictionary2
dictionary2 = PyDictionary("exclusive","precipitation")
# Finding Synonym using Dictionary1
print(dictionary1.meaning('Archive'))
# Finding Synonyms of word in Dictionary2
print(dictionary2.printMeanings()) 
# Finding antonyms using dictionary1
print(dictionary1.synonym("Archive"))
# Finding antonyms using dictionary2
print (dictionary2.getSynonyms())
# Translating using Dictionary1
dictionary1.antonym("Archive")
print (dictionary2.getAntonyms())
# Translating words in dictionary2
dictionary1.translate("Archive", "hi")
print (dictionary2.translateTo("hi"))
