

MyString = ''
with open("test.txt") as MyFile:
    for Line in MyFile:
        MyString += Line
    
MyString = MyString.replace('\n','')
MySentences = MyString.split('. ')
MyList = []
for Sentence in MySentences:
    if Sentence[-1] == '.':
        MyList.append(Sentence.capitalize())
    else:
        MyList.append(Sentence.capitalize() + '.')

MyWords = []
for Sentence in MyList:
    MyWords.extend(Sentence.split())

print("Writing file.")
with open("output.txt","w+") as MyFile:
    LineLength = 0
    for Word in MyWords:
        if LineLength + len(Word) > 80:
            MyFile.write('\n')
            LineLength = 0
        MyFile.write(Word + ' ')
        LineLength += len(Word) + 1
print("File written")

CSVData = []
with open("Test.csv") as MyFile:
    for Line in MyFile:
        CSVData.append(Line.split(','))

print(CSVData)
