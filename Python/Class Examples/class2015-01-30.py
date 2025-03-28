LetterDictionary = {}
for Char in range(65,91):
    if Char >= ord('S'):
        if Char == 90:
            LetterDictionary['Z'] = '9'
        else:
            LetterDictionary[chr(Char)] = chr((Char - 66)//3 + ord('2'))
    else:
        LetterDictionary[chr(Char)] = chr((Char - 65)//3 + ord('2'))

def NumCheck(unformatted_number):
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


def FormatPhoneNumber(unformatted_number,default_area=530,default_prefix=75):
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

def InputPhoneNumber(name_in_book):
    while True:
        NewNumber = input('Enter number for %s> '%name_in_book)
        if NumCheck(NewNumber):
            return FormatPhoneNumber(NewNumber)
        else:
            print('"%s" is not a valid number'%name_in_book)

def InputName(prompt_text):
    while True:
        Name = input('%s> '%prompt_text).strip()
        if len(Name) == 0:
            print('Please enter a valid name.')
        else:
            return Name

def SearchPhonebook(search_name):
    PossibleNames = []
    for Name in PhoneBook:
        if Name.find(search_name) >= 0:
            PossibleNames.append(Name)
    if len(PossibleNames) == 1:
        return PossibleNames[0]
    print('%s not found in phone book\nDid you mean?'%search_name)
    for Name in PossibleNames:
        print(NameTranslation[Name])
    return ''

PhoneBook = {}
PhoneBook['cs phone'] = '(530) 752-7004'
PhoneBook['cs fax'] = '(530) 752-4767'
PhoneBook['ece phone'] = '(530) 752-0583'
PhoneBook['ucd phone'] = '(530) 752-1011'
PhoneBook['ee phone'] = '(530) 752-0583'
NameTranslation = {}
NameTranslation['cs phone'] = 'CS Phone'
NameTranslation['cs fax'] = 'CS Fax'
NameTranslation['ece phone'] = 'ECE Phone'
NameTranslation['ucd phone'] = 'UCD Phone'
NameTranslation['ee phone'] = 'EE Phone'

Done = False
while not Done:
    print('L List names in phonebook')
    print('S Search number')
    print('A Add a number')
    print('E Edit a number')
    print('R Remove a number')
    print('Q Quit')
    print('-----------------')
    Command = ''
    while Command == '':
        Command = input("Enter a choice> ")
        Command = Command.strip().upper()
    if Command[0] == 'L':
        print('Names in phonebook:')
        for Name in NameTranslation:
            print(NameTranslation[Name])
        print('')
    elif Command[0] == 'S':
        SearchName = InputName('Enter a name')
        if SearchName.lower() not in PhoneBook:
            SearchName = SearchPhonebook(SearchName)
            if len(SearchName):
                print('Phone number for %s is %s'%(NameTranslation[SearchName.lower()], PhoneBook[SearchName.lower()]))
        else:
            print('Phone number is',PhoneBook[SearchName.lower()])
    elif Command[0] == 'A':
        NewName = InputName('Enter name to add')
        if NewName.lower() in PhoneBook:
            print(NewName, 'already in phonebook')
        else:
            PhoneBook[NewName.lower()] = InputPhoneNumber(NewName)
            NameTranslation[NewName.lower()] = NewName
    elif Command[0] == 'E':
        EditName = InputName('Enter name to edit')
        if EditName.lower() not in PhoneBook:
            print(EditName, 'is not in the phonebook')
        else:
            PhoneBook[EditName.lower()] = InputPhoneNumber(NameTranslation[EditName.lower()])
    elif Command[0] == 'R':
        RemoveName = InputName('Enter name to remove')
        if RemoveName.lower() not in PhoneBook:
            print(RemoveName, 'is not in the phonebook')
        else:
            del PhoneBook[RemoveName.lower()]
            print(NameTranslation[RemoveName.lower()],'was removed from phonebook')
            del NameTranslation[RemoveName.lower()]
    elif Command[0] == 'Q':
        Done = True

        
