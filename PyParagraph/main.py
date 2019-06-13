import os
import re

filepath = os.path.join("raw_data","paragraph_2.txt")

#Open the file and append each word into array
#str1=[]
#with open(filepath, "r", encoding="UTF-8") as fp:
#    for line in fp:
#        for words in line.split():
#            str1.append(words)

#Using list comprehension makes it more concise
with open(filepath, "r", encoding="UTF-8") as fp:
    str = [words for line in fp for words in line.split()]

##Do the calculations

#Determine the total number of letters in input file.
strlen = 0
for words in str:
    strlen += len(words)

#Create a paragraph element which is the input file stripped of all new lines.
paragraph = " ".join(str)

#Identify the total number of sentences
sentencecount = re.split("(?<=[.!?]) +", paragraph)

#Total number of words is the number of 
totalNumberOfWords = len(str)

print("Paragraph Analysis")
print("-" * 35)
print(f"Approximate word count = {totalNumberOfWords}")
print(f"Approximate Sentence Count: {len(sentencecount)}")
print(f"Average Letter Count = {strlen/totalNumberOfWords:2.2f}")
print(f"Average sentence Length = {totalNumberOfWords/len(sentencecount):2.2f}")
print("-" * 35)