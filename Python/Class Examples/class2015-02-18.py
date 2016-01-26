LetterDictionary = {}
for Char in range(65,91):
    if Char >= ord('S'):
        if Char == 90:
            LetterDictionary['Z'] = '9'
        else:
            LetterDictionary[chr(Char)] = chr((Char - 66)//3 + ord('2'))
    else:
        LetterDictionary[chr(Char)] = chr((Char - 65)//3 + ord('2'))

class Phonebook:
    def __init__(self,name_of_phonebook):
        self.Name = name_of_phonebook
        self.Name2Number = {}
        self.NameTranslation = {}
        if name_of_phonebook.lower() == 'work':
            self.Name2Number['cs phone'] = '(530) 752-7004'
            self.Name2Number['cs fax'] = '(530) 752-4767'
            self.Name2Number['ece phone'] = '(530) 752-0583'
            self.Name2Number['ucd phone'] = '(530) 752-1011'
            self.Name2Number['ee phone'] = '(530) 752-0583'
            
            self.NameTranslation['cs phone'] = 'CS Phone'
            self.NameTranslation['cs fax'] = 'CS Fax'
            self.NameTranslation['ece phone'] = 'ECE Phone'
            self.NameTranslation['ucd phone'] = 'UCD Phone'
            self.NameTranslation['ee phone'] = 'EE Phone'
        
    def NumCheck(self,unformatted_number):
        TempNumber = ''
        for AnyNumber in unformatted_number.upper():
            if ('0' <= AnyNumber) and ('9' >= AnyNumber):
                TempNumber = TempNumber + AnyNumber
            if ('A' <= AnyNumber) and ('Z' >= AnyNumber):
                TempNumber = TempNumber + AnyNumber
        if len(TempNumber) < 5:
            return False
        if len(TempNumber) > 10:
            return False
        if len(TempNumber) in [6, 8, 9]:
            return False
        if len(TempNumber) in [7, 10]:
            if TempNumber[0] == '0' or TempNumber[0] == '1':
                return False
            if len(TempNumber) == 10:
                if TempNumber[3] == '0' or TempNumber[3] == '1':
                    return False
        return True


    def FormatPhoneNumber(self,unformatted_number,default_area=530,default_prefix=75):
        TempNumber = ''
        for AnyNumber in unformatted_number.upper():
            if ('0' <= AnyNumber) and ('9' >= AnyNumber):
                TempNumber = TempNumber + AnyNumber
            if ('A' <= AnyNumber) and ('Z' >= AnyNumber):
                TempNumber = TempNumber + LetterDictionary[AnyNumber]
        FullNumber = int(TempNumber)
        if 9999999 < FullNumber:
            AreaCode = int(TempNumber[0:3])
        elif 99999 < FullNumber:
            AreaCode = default_area
        else:
            AreaCode = default_area
            FullNumber += default_prefix * 100000
        Prefix = (FullNumber // 10000) % 1000
        Suffix = FullNumber % 10000
        FormattedNumber = '(%d) %03d-%04d'%(AreaCode,Prefix,Suffix)
        return FormattedNumber

    def InputPhoneNumber(self,name_in_book):
        while True:
            NewNumber = input('Enter number for %s> '%name_in_book)
            if self.NumCheck(NewNumber):
                return self.FormatPhoneNumber(NewNumber)
            else:
                print('"%s" is not a valid number'%NewNumber)

    def InputName(self,prompt_text):
        while True:
            Name = input('%s> '%prompt_text).strip()
            if len(Name) == 0:
                print('Please enter a valid name.')
            else:
                return Name

    def SearchPhonebook(self,search_name):
        SearchTerms = search_name.lower().split('*')
        if len(SearchTerms) == 1:
            return []
        PossibleNames = []
        for Name in self.Name2Number:
            AllTermsMatch = True
            Start = 0
            FirstSearch = True
            for Term in SearchTerms:
                FindLocation = Name.find(Term,Start)
                if FindLocation < 0:
                    AllTermsMatch = False
                    break
                if FirstSearch and FindLocation != 0:
                    AllTermsMatch = False
                    break
                FirstSearch = False
                Start = FindLocation+len(Term)
            
            if len(SearchTerms[-1]):
                if SearchTerms[-1] != Name[-len(SearchTerms[-1]):]:
                    AllTermsMatch = False
                
            if AllTermsMatch:
                PossibleNames.append(Name)

        return PossibleNames

    def SearchName(self):
        SearchName = self.InputName('Enter a name')
        if SearchName.lower() not in self.Name2Number:
            PossibleNames = self.SearchPhonebook(SearchName)
            if len(PossibleNames) == 1:
                print("Did you mean?")
                print('Phone number for %s is %s'%(self.NameTranslation[PossibleNames[0].lower()], self.Name2Number[PossibleNames[0].lower()]))
            elif len(PossibleNames):
                print("Did you mean?")
                for Name in PossibleNames:
                    print(" ",self.NameTranslation[Name])
            else:
                print("No match found for %s!"%SearchName)
        else:
            print('Phone number is',self.Name2Number[SearchName.lower()])

    def AddName(self):
        NewName = self.InputName('Enter name to add')
        if NewName.lower() in self.Name2Number:
            print(NewName, 'already in phonebook')
        else:
            self.Name2Number[NewName.lower()] = self.InputPhoneNumber(NewName)
            self.NameTranslation[NewName.lower()] = NewName

    def EditNumber(self):
        EditName = self.InputName('Enter name to edit')
        if EditName.lower() not in self.Name2Number:
            print(EditName, 'is not in the phonebook')
        else:
            self.Name2Number[EditName.lower()] = self.InputPhoneNumber(self.NameTranslation[EditName.lower()])

    def RemoveNumber(self):
        RemoveName = self.InputName('Enter name to remove')
        if RemoveName.lower() not in self.Name2Number:
            print(RemoveName, 'is not in the phonebook')
        else:
            del self.Name2Number[RemoveName.lower()]
            print(self.NameTranslation[RemoveName.lower()],'was removed from phonebook')
            del self.NameTranslation[RemoveName.lower()]

    def ListNames(self):
        print('Names in phonebook:')
        for Name in self.NameTranslation:
            print(self.NameTranslation[Name])
        print('')

    def SaveToFile(self,filename):
        with open(filename,'w') as MyFile:
            for Name in self.Name2Number:
                MyFile.write(self.NameTranslation[Name] + ',' + self.Name2Number[Name] + '\n')
            

if __name__ == '__main__':
    MyWorkPhonebook = Phonebook('Work')
    MyHomePhonebook = Phonebook('Home Phone')
    MyCurrentPhonebook = MyWorkPhonebook 
    Done = False
    MenuChoices = {}
    MenuChoices['C'] = 'Change phonebook'
    MenuChoices['L'] = 'List names in phonebook'
    MenuChoices['S'] = 'Search number'
    MenuChoices['A'] = 'Add a number'
    MenuChoices['E'] = 'Edit a number'
    MenuChoices['R'] = 'Remove a number'
    MenuChoices['W'] = 'Write to file'
    MenuChoices['Q'] = 'Quit'
    MenuOrder = ['C', 'L', 'S', 'A', 'E', 'R', 'W', 'Q']
    while not Done:
        MaxLength = 0
        for Value in MenuChoices.values():
            MaxLength = max(MaxLength, len(Value) + 2)
        Dashcount = ((MaxLength-len(MyCurrentPhonebook.Name)-2)//2)
        if MaxLength % 2 == 1:
            print('-'*Dashcount,MyCurrentPhonebook.Name+' ','-'*Dashcount)
        else:
            
            print('-'*Dashcount,MyCurrentPhonebook.Name,'-'*Dashcount)
        for Item in MenuOrder:
            print(Item,MenuChoices[Item])
        
        print('-'*MaxLength)
        Command = ' '
        while Command[0] not in MenuChoices.keys():
            Command = input("Enter a choice> ")
            Command = Command.strip().upper()
            if not Command:
                Command = ' '
            
        if Command[0] == 'C':
            if MyCurrentPhonebook is MyWorkPhonebook:
                MyCurrentPhonebook = MyHomePhonebook
            else:
                MyCurrentPhonebook = MyWorkPhonebook
        elif Command[0] == 'L':
            MyCurrentPhonebook.ListNames()
        elif Command[0] == 'S':
            MyCurrentPhonebook.SearchName()
        elif Command[0] == 'A':
            MyCurrentPhonebook.AddName()
        elif Command[0] == 'E':
            MyCurrentPhonebook.EditNumber()
        elif Command[0] == 'R':
            MyCurrentPhonebook.RemoveNumber()
        elif Command[0] == 'W':
            Filename = ''
            while Filename == '':
                Filename = input("Enter filename> ")
            MyCurrentPhonebook.SaveToFile(Filename)
        elif Command[0] == 'Q':
            Done = True

        
