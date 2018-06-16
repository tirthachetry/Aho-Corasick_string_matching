import PyPDF2
import pandas as pd
from flashtext.keyword import KeywordProcessor

#loading the pdf for reading 
pdfFileObj = open('JavaBasics-notes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
num_pages = pdfReader.numPages
count = 0
text = ""
while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count +=1
    text += pageObj.extractText()


#now part for Java-keywords
#aho-corasick algorithm for string matching
#trie data-structure
keywords = open("keywords.txt","r")
keys=keywords.read().splitlines()
keyword_processor = KeywordProcessor()
for i in range(len(keys)):
    keyword_processor.add_keyword(keys[i])
    keywords_found = keyword_processor.extract_keywords(text)
found=keywords_found


# Given a list of words, return a dictionary of
# word-frequency pairs.
def wordListToFreqDict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(zip(wordlist,wordfreq))


# Sort a dictionary of word-frequency pairs in
# order of descending frequency.
def sortFreqDict(freqdict):
    aux = [(freqdict[key], key) for key in freqdict]
    aux.sort()
    aux.reverse()
    return aux

#creating a dictionary
dictionaryA = sortFreqDict(wordListToFreqDict(found)) 

#save to excel file
df=pd.DataFrame.from_dict(dictionaryA)
writer = pd.ExcelWriter('output.xlsx')
df.to_excel(writer,'Sheet1',header=['occurence','keyword'],index=False)
writer.save()




















