
from class_phonebook import *

class AddressPhoneBook(Phonebook):

    def __init__(self, name_of_book):
        Phonebook.__init__(self,name_of_book)
        self.Name2Address = {}
        if name_of_book == 'Work':
            self.Name2Address['cs phone'] = '2063 Kemper Hall'
            self.Name2Address['cs fax'] = '2063 Kemper Hall'
            self.Name2Address['ece phone'] = '2064 Kemper Hall'
            self.Name2Address['ucd phone'] = 'One Shields Ave.'
            self.Name2Address['ee phone'] = '2064 Kemper Hall'

    def SearchName(self):
        SearchName = self.InputName('Enter a name')
        if SearchName.lower() not in self.Name2Number:
            PossibleNames = self.SearchPhonebook(SearchName)
            if len(PossibleNames) == 1:
                print("Did you mean?")
                print('Phone number for %s is %s, at %s'%(self.NameTranslation[PossibleNames[0].lower()], self.Name2Number[PossibleNames[0].lower()], self.Name2Address[PossibleNames[0].lower()]))
            elif len(PossibleNames):
                print("Did you mean?")
                for Name in PossibleNames:
                    print(" ",self.NameTranslation[Name])
            else:
                print("No match found for %s!"%SearchName)
        else:
            print('Phone number is',self.Name2Number[SearchName.lower()])
            print('Address is',self.Name2Address[SearchName.lower()])

    def InputAddress(self,name_in_book):
        while True:
            NewAddress = input('Enter address for %s> '%name_in_book).strip()
            if NewAddress != '':
                return NewAddress
            else:
                print('"%s" is not a valid address'%NewAddress)

    def AddName(self):
        NewName = self.InputName('Enter name to add')
        if NewName.lower() in self.Name2Number:
            print(NewName, 'already in phonebook')
        else:
            self.Name2Number[NewName.lower()] = self.InputPhoneNumber(NewName)
            self.Name2Address[NewName.lower()] = self.InputAddress(NewName)
            self.NameTranslation[NewName.lower()] = NewName

    def EditAddress(self):
        EditName = self.InputName('Enter name to edit')
        if EditName.lower() not in self.Name2Number:
            print(EditName, 'is not in the phonebook')
        else:
            self.Name2Address[EditName.lower()] = self.InputAddress(self.NameTranslation[EditName.lower()])

    def RemoveNumber(self):
        RemoveName = self.InputName('Enter name to remove')
        if RemoveName.lower() not in self.Name2Number:
            print(RemoveName, 'is not in the phonebook')
        else:
            del self.Name2Number[RemoveName.lower()]
            del self.Name2Address[RemoveName.lower()]
            print(self.NameTranslation[RemoveName.lower()],'was removed from phonebook')
            del self.NameTranslation[RemoveName.lower()]

    def SaveToFile(self,filename):
        with open(filename,'w') as MyFile:
            MyFile.write('Name,Phone,Address\n')
            for Name in self.Name2Number:
                MyFile.write(self.NameTranslation[Name] + ',' + self.Name2Number[Name] + ',' + self.Name2Address[Name] + '\n')
        
    def LoadFromFile(self,filename):            
        with open(filename) as MyFile:
            self.Name2Number = {}
            self.NameTranslation = {}
            self.Name2Address = {}
            FirstLine = True
            ColumnMapping = {}
            for Line in MyFile:
                if FirstLine:
                    EntryList = Line.replace('\n','').split(',')
                    for Index, Entry in enumerate(EntryList):
                        ColumnMapping[Entry] = Index
                    FirstLine = False
                else:
                    EntryList = Line.replace('\n','').split(',')
                    self.Name2Number[EntryList[ColumnMapping['Name']].lower()] = EntryList[ColumnMapping['Phone']]
                    self.NameTranslation[EntryList[ColumnMapping['Name']].lower()] = EntryList[ColumnMapping['Name']]
                    self.Name2Address[EntryList[ColumnMapping['Name']].lower()] = EntryList[ColumnMapping['Address']]



if __name__ == '__main__':
    MyWorkPhonebook = AddressPhoneBook('Work')
    MyHomePhonebook = AddressPhoneBook('Home Phone')
    MyCurrentPhonebook = MyWorkPhonebook 
    Done = False
    MenuChoices = {}
    MenuChoices['C'] = 'Change phonebook'
    MenuChoices['L'] = 'List names in phonebook'
    MenuChoices['S'] = 'Search number'
    MenuChoices['A'] = 'Add a listing'
    MenuChoices['E'] = 'Edit a number'
    MenuChoices['D'] = 'Edit address'
    MenuChoices['R'] = 'Remove a listing'
    MenuChoices['W'] = 'Write to file'
    MenuChoices['I'] = 'Input from file'
    MenuChoices['Q'] = 'Quit'
    MenuOrder = ['C', 'L', 'S', 'A', 'E', 'D', 'R', 'W', 'I', 'Q']
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
        elif Command[0] == 'D':
            MyCurrentPhonebook.EditAddress()
        elif Command[0] == 'R':
            MyCurrentPhonebook.RemoveNumber()
        elif Command[0] == 'W':
            Filename = ''
            while Filename == '':
                Filename = input("Enter filename> ")
            MyCurrentPhonebook.SaveToFile(Filename)
        elif Command[0] == 'I':
            Filename = ''
            while Filename == '':
                Filename = input("Enter filename> ")
            MyCurrentPhonebook.LoadFromFile(Filename)
        elif Command[0] == 'Q':
            Done = True
