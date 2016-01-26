
MyString = ''
with open('test.txt') as MyFile:
    for Line in MyFile:
        MyString += Line # MyString = MyString + Line

MyString = MyString.replace('\n','')
MySentences = MyString.split('. ')
MyList = []
for Sentence in MySentences:
    if Sentence[-1] == '.':
        MyList.append(Sentence.capitalize())
    else:
        MyList.append(Sentence.capitalize() + '.')


with open('output.txt','w') as Variable:
    LineLength = 0
    for Sentence in MyList:
        for Word in Sentence.split():
            if LineLength + len(Word)  > 80:
                Variable.write('\n')
                LineLength = 0
            Variable.write(Word)
            LineLength += len(Word)
            if LineLength != 80:
                Variable.write(' ')
                LineLength += 1

with open('Test.csv') as MyVariable:
    for Line in MyVariable:
        print(Line.replace('\n','').split(','))
