import os

class PhoneNumber:
    LetterDictionary = {}
    for Char in range(65,91):
        if Char >= ord('S'):
            if Char == 90:
                LetterDictionary['Z'] = '9'
            else:
                LetterDictionary[chr(Char)] = chr((Char - 66)//3 + ord('2'))
        else:
            LetterDictionary[chr(Char)] = chr((Char - 65)//3 + ord('2'))

    DisplayName = 'Phone Number'
    
    def __init__(self):
        self.AreaCode = 530
        self.Prefix = 752
        self.Suffix = 1

    def __str__(self):
        return '(%d) %d-%04d'%(self.AreaCode,self.Prefix,self.Suffix)

    def Assign(self, other):
        self.AreaCode = other.AreaCode
        self.Prefix = other.Prefix
        self.Suffix = other.Suffix

    def IsValid(phonenumber_as_string):
        if type(phonenumber_as_string) != str:
            return False
        CheckNumber = ''
        for Char in phonenumber_as_string.upper():
            if Char.isnumeric():
                CheckNumber += Char
            if Char.isalpha():
                CheckNumber += PhoneNumber.LetterDictionary[Char]
        if CheckNumber == '':
            return False
        CheckNumber = int(CheckNumber)
        Suffix = CheckNumber % 10000
        CheckNumber = CheckNumber // 10000
        Prefix = CheckNumber % 1000
        AreaCode = CheckNumber // 1000
        if AreaCode and (AreaCode < 200):
            return False
        if (Prefix >= 10) and (Prefix < 200):
            return False
        if AreaCode and (Prefix < 10):
            return False
        return True

    def Parse(self, phonenumber_as_string):
        if PhoneNumber.IsValid(phonenumber_as_string):
            CheckNumber = ''
            for Char in phonenumber_as_string.upper():
                if Char.isnumeric():
                    CheckNumber += Char
                if Char.isalpha():
                    CheckNumber += PhoneNumber.LetterDictionary[Char]

            CheckNumber = int(CheckNumber)
            Suffix = CheckNumber % 10000
            CheckNumber = CheckNumber // 10000
            Prefix = CheckNumber % 1000
            AreaCode = CheckNumber // 1000
            self.AreaCode = 530
            if AreaCode:
                self.AreaCode = AreaCode
            self.Prefix = Prefix
            if Prefix < 10:
                self.Prefix += 750
            self.Suffix = Suffix

class Address:
    DisplayName = 'Address'

    def __init__(self):
        self.Street1 = 'One Shields Ave.'
        self.Street2 = '2063 Kemper Hall'
        self.City = 'Davis'
        self.State = 'CA'
        self.ZipCode = 95616
        self.ZipPlus4 = -1

    def Assign(self, other):
        self.Street1 = other.Street1
        self.Street2 = other.Street2
        self.City = other.City
        self.State = other.State
        self.ZipCode = other.ZipCode
        self.ZipPlus4 = other.ZipPlus4
        
    def __str__(self):
        ReturnString = self.Street1 + ', '
        if self.Street2 != '':
            ReturnString += self.Street2 + ', '
        ReturnString += self.City + ', ' + self.State + ' '
        ReturnString += '%05d'%self.ZipCode
        if self.ZipPlus4 >= 0:
            ReturnString +=  '-%04d'%self.ZipPlus4
        return ReturnString

    def IsValid(newaddress):
        Components = newaddress.split(',')
        if len(Components) < 3:
            return False
        if len(Components) > 4:
            return False
        CityZip = Components[-1].split()
        if len(CityZip[0]) != 2:
            return False
        ZipValues = CityZip[-1].split('-')
        if len(ZipValues[0]) != 5:
            return False
        if len(ZipValues) > 1 and len(ZipValues[-1]) != 4:
            return False
        return True
    
    def Parse(self,address_as_string):
        if Address.IsValid(address_as_string):
            Components = address_as_string.split(',')
            self.Street1 = Components[0].strip()
            if len(Components) == 4:
                self.Street2 = Components[1].strip()
            else:
                self.Street2 = ''
            self.City = Components[-2].strip()
            StateZip = Components[-1].split()
            self.State = StateZip[0].strip()
            ZipCodePlus4 = StateZip[1].split('-')
            
            self.ZipCode = int(ZipCodePlus4[0])
            if len(ZipCodePlus4) > 1:
                self.ZipPlus4 = int(ZipCodePlus4[1])
            else:
                self.ZipPlus4 = -1
            return True

        return False

class EmailAddress:
    DisplayName = 'E-mail Address'
    def __init__(self):
        self.Address = 'cjnitta@ucdavis.edu'

    def __str__(self):
        return self.Address

    def Assign(self, other):
        self.Address = other.Address

    def IsValid(email_as_string):
        EmailParts = email_as_string.split('@')
        if len(EmailParts) != 2:
            return False
        if EmailParts[0] == '':
            return False
        DomainParts = EmailParts[1].split('.')
        if len(DomainParts) < 2:
            return False
        for SubDomain in DomainParts:
            if SubDomain == '':
                return False
        return 2 <= len(DomainParts[-1]) <= 4
        
    def Parse(self, email_as_string):
        if EmailAddress.IsValid(email_as_string):
            self.Address = email_as_string
            return True
        return False

class Contact:
    def __init__(self):
        self.ClearAll()

    def ClearAll(self):
        self.FirstName = ''
        self.LastName = ''
        self.PhoneNumbers = {}
        self.Addresses = {}
        self.EmailAddresses = {}        

    def HasPhoneNumber(self,type_of_number):
        return type_of_number in self.PhoneNumbers

    def GetPhoneNumber(self,type_of_number):
        if type_of_number in self.PhoneNumbers:
            return self.PhoneNumbers[type_of_number]
        else:
            return PhoneNumber()

    def SetPhoneNumber(self,type_of_number,new_number):
        if type(new_number) == int or type(new_number) == str:
            NewNumberString = str(new_number)
            if PhoneNumber.IsValid(NewNumberString):
                NewPhoneNumber = PhoneNumber()
                NewPhoneNumber.Parse(NewNumberString)
                self.PhoneNumbers[type_of_number] = NewPhoneNumber
        elif type(new_number) == PhoneNumber:
            NewPhoneNumber = PhoneNumber()
            NewPhoneNumber.Assign(new_number)
            self.PhoneNumbers[type_of_number] = NewPhoneNumber
            
    def RemovePhoneNumber(self,type_of_number):
        if type_of_number in self.PhoneNumbers:
            del self.PhoneNumbers[type_of_number]
        
    def HasAddress(self,type_of_address):
        return type_of_address in self.Addresses

    def GetAddress(self,type_of_address):
        if type_of_address in self.Addresses:
            return self.Addresses[type_of_address]
        else:
            return Address()

    def SetAddress(self,type_of_address,new_address):
        if type(new_address) == str:
            if Address.IsValid(new_address):
                NewAddress = Address()
                NewAddress.Parse(new_address)
                self.Addresses[type_of_address] = NewAddress
        elif type(new_address) == Address:
            NewAddress = Address()
            NewAddress.Assign(new_address)
            self.Addresses[type_of_address] = NewAddress
            
    def RemoveAddress(self,type_of_address):
        if type_of_address in self.Addresses:
            del self.Addresses[type_of_address]


    def HasEmailAddress(self,type_of_address):
        return type_of_address in self.EmailAddresses

    def GetEmailAddress(self,type_of_address):
        if type_of_address in self.EmailAddresses:
            return self.EmailAddresses[type_of_address]
        else:
            return EmailAddress()

    def SetEmailAddress(self,type_of_address,new_address):
        if type(new_address) == str:
            if EmailAddress.IsValid(new_address):
                NewAddress = EmailAddress()
                NewAddress.Parse(new_address)
                self.EmailAddresses[type_of_address] = NewAddress
        elif type(new_address) == EmailAddress:
            NewAddress = EmailAddress()
            NewAddress.Assign(new_address)
            self.EmailAddresses[type_of_address] = NewAddress
            
    def RemoveEmailAddress(self,type_of_address):
        if type_of_address in self.EmailAddresses:
            del self.EmailAddresses[type_of_address]

    def MenuAndChoice(menu):
        AllChoices = []
        for Item in menu:
            print(Item[0],Item[1])
            AllChoices.append(Item[0])
        Choice = ''
        while Choice not in AllChoices:
            Choice = input('Enter Choice> ').upper().strip()
        return Choice
        
    def ModifyContact(self):
        Options = []
        Options.append(('A','Add Information'))
        Options.append(('E','Edit Information'))
        Options.append(('R','Remove Information'))
        Options.append(('S','Save To File'))
        Options.append(('L','Load From File'))
        Options.append(('D','Done'))
            
        while True:
            Choice = Contact.MenuAndChoice(Options)
            if Choice == 'A':
                self.AddInformation()
            elif Choice == 'E':
                self.EditInformation()
            elif Choice == 'R':
                self.RemoveInformation()
            elif Choice == 'S':
                FileName = input('Enter Filename> ')
                self.SaveToFile(FileName)
            elif Choice == 'L':
                FileName = input('Enter Filename> ')
                self.LoadFromFile(FileName)
            else:
                return
            
    def AddInformation(self):
        Options = []
        Options.append(('1','Add Phone Number'))
        Options.append(('2','Add Address'))
        Options.append(('3','Add E-mail Address'))
        Options.append(('B','Back'))
        while True:
            Choice = Contact.MenuAndChoice(Options)
            if Choice == '1':
                self.AddEditSpecificInformation(Contact.HasPhoneNumber,Contact.SetPhoneNumber,PhoneNumber)
            elif Choice == '2':
                self.AddEditSpecificInformation(Contact.HasAddress,Contact.SetAddress,Address)
            elif Choice == '3':
                self.AddEditSpecificInformation(Contact.HasEmailAddress,Contact.SetEmailAddress,EmailAddress)
            else:
                return
            
    def AddEditSpecificInformation(self,has_func,set_func,class_type,already_has=False):
        InfoType = input('Enter type of %s> '%class_type.DisplayName)
        if has_func(self,InfoType) != already_has:
            if already_has:
                print('%s %s does not have a %s %s'%(self.FirstName, self.LastName,InfoType,class_type.DisplayName))
            else:                            
                print('%s %s already has a %s %s'%(self.FirstName, self.LastName,InfoType,class_type.DisplayName))
            return
        Information = ''
        while not class_type.IsValid(Information):
            Information = input('Enter %s %s> '%(InfoType,class_type.DisplayName))

        NewInformation = class_type()
        NewInformation.Parse(Information)
        set_func(self,InfoType,NewInformation)
        print(InfoType, Information)       
    
            
    def EditInformation(self):
        Options = []
        Options.append(('1','Edit Name'))
        Options.append(('2','Edit Phone Number'))
        Options.append(('3','Edit Address'))
        Options.append(('4','Edit E-mail Address'))
        Options.append(('B','Back'))
        while True:
            Choice = Contact.MenuAndChoice(Options)
            if Choice == '1':
                self.EditName()
            elif Choice == '2':
                self.AddEditSpecificInformation(Contact.HasPhoneNumber,Contact.SetPhoneNumber,PhoneNumber,True)
            elif Choice == '3':
                self.AddEditSpecificInformation(Contact.HasAddress,Contact.SetAddress,Address,True)
            elif Choice == '4':
                self.AddEditSpecificInformation(Contact.HasEmailAddress,Contact.SetEmailAddress,EmailAddress,True)
            else:
                return
            
    def EditName(self):
        NewFirst = ''
        while NewFirst == '':
            NewFirst = input('Enter new first name for %s %s> '%(self.FirstName,self.LastName))
            NewFirst = NewFirst.strip()
        NewLast = ''
        while NewLast == '':
            NewLast = input('Enter new last name for %s %s> '%(self.FirstName,self.LastName))
            NewLast = NewLast.strip()
        self.FirstName = NewFirst
        self.LastName = NewLast
    
    def RemoveInformation(self):
        Options = []
        Options.append(('1','Remove Phone Number'))
        Options.append(('2','Remove Address'))
        Options.append(('3','Remove E-mail Address'))
        Options.append(('B','Back'))
        while True:
            Choice = Contact.MenuAndChoice(Options)
            if Choice == '1':
                self.RemoveSpecificInformation(Contact.HasPhoneNumber,Contact.RemovePhoneNumber,PhoneNumber)
            elif Choice == '2':
                self.RemoveSpecificInformation(Contact.HasAddress,Contact.RemoveAddress,Address)
            elif Choice == '3':
                self.RemoveSpecificInformation(Contact.HasEmailAddress,Contact.RemoveEmailAddress,EmailAddress)
            else:
                return
    def RemoveSpecificInformation(self,has_func,remove_func,class_type,):
        InfoType = input('Enter type of %s to remove> '%class_type.DisplayName)
        if not has_func(self,InfoType):
            print('%s %s does not have a %s %s'%(self.FirstName, self.LastName,InfoType,class_type.DisplayName))
            return
        remove_func(self,InfoType)

    def SaveToFile(self,filename):
        with open(filename,'w') as OutFile:
            OutFile.write('First Name\t' + self.FirstName + '\n')
            OutFile.write('Last Name\t' + self.LastName + '\n')
            for Key,Value in self.PhoneNumbers.items():
                OutFile.write(Key + ' Phone\t' + str(Value) + '\n')
            for Key,Value in self.Addresses.items():
                OutFile.write(Key + ' Address\t' + str(Value) + '\n')
            for Key,Value in self.EmailAddresses.items():
                OutFile.write(Key + ' E-mail\t' + str(Value) + '\n')
            
    def LoadFromFile(self,filename):
        try:
            self.ClearAll()
            with open(filename) as InFile:
                NewDictionary = {}
                for Line in InFile:
                    Elements = Line.replace('\n','').split('\t')
                    NewDictionary[Elements[0]] = Elements[1]
                self.LoadFromDictionary(NewDictionary)
        except FileNotFoundError:
            print('Could not load file %s.'%filename)
            
    def LoadFromDictionary(self,my_dict):
        self.ClearAll()
        
        for Key,Value in my_dict.items():
            if Key== 'First Name':
                self.FirstName = Value
            elif Key == 'Last Name':
                self.LastName = Value
            elif Key.rfind('Phone') == len(Key) - 5:
                #print(Elements[0],Elements[1])
                self.SetPhoneNumber(Key[:-5].strip(),Value)
            elif Key.rfind('Address') == len(Key) - 7:
                #print(Elements[0],Elements[1])
                self.SetAddress(Key[:-7].strip(),Value)
            elif Key.rfind('E-mail') == len(Key) - 6:
                #print(Elements[0],Elements[1])
                self.SetEmailAddress(Key[:-6].strip(),Value)
            #print(Elements)        

class VeryCoolName:
    def __init__(self):
        self.VeryCoolDictionary = {}

    def VeryCoolMenu(self):
        Options = []
        Options.append(('A','Add Contact'))
        Options.append(('E','Edit Contact'))
        Options.append(('R','Remove Contact'))
        Options.append(('L','Load Contacts From File'))
        Options.append(('S','Save Contacts To File'))
        Options.append(('D','Done'))
        while True:
            Choice = Contact.MenuAndChoice(Options)
            if Choice == 'A':
                NewContact = Contact()
                NewContact.ModifyContact()
                self.VeryCoolDictionary[(NewContact.FirstName+' '+NewContact.LastName).lower()] = NewContact
            elif Choice == 'E':
                AnAmazingName = input('Enter a name> ').strip()
                if AnAmazingName.lower() in self.VeryCoolDictionary:
                    self.VeryCoolDictionary[AnAmazingName.lower()].ModifyContact()
                else:
                    print('%s is not in the contact list.'%AnAmazingName)
            elif Choice == 'R':
                AnAmazingName = input('Enter a name> ').strip()
                if AnAmazingName.lower() in self.VeryCoolDictionary:
                    del self.VeryCoolDictionary[AnAmazingName.lower()]
                else:
                    print('%s is not in the contact list.'%AnAmazingName)
            elif Choice == 'L':
                FileName = input('Enter a filename> ')
                self.LoadFromFile(FileName)
            elif Choice == 'S':
                FileName = input('Enter a filename> ')
                self.SaveToFile(FileName)
            elif Choice == 'D':
                break
            
    def LoadFromFile(self, filename):
        try:
            self.VeryCoolDictionary = {}
            with open(filename) as InFile:
                NewDictionary = {}
                FirstLine = True
                
                for Line in InFile:
                    if FirstLine:
                        ListOfHeadings = Line.replace('\n','').split('\t')
                        FirstLine = False
                    else:
                        Elements = Line.replace('\n','').split('\t')
                        NewDictionary = {}
                        for Index,Item in enumerate(ListOfHeadings):
                            if Elements[Index] != '':
                                NewDictionary[Item] = Elements[Index]
                        NewContact = Contact()
                        NewContact.LoadFromDictionary(NewDictionary)
                        self.VeryCoolDictionary[(NewContact.FirstName+' '+NewContact.LastName).lower()] = NewContact
        except FileNotFoundError:
            print('Could not load file %s.'%filename)
            
    def SaveToFile(self, filename):
        PhoneTypes = {}
        AddressTypes = {}
        EmailTypes = {}
        for Contact in self.VeryCoolDictionary.values():
            for Phone in Contact.PhoneNumbers:
                PhoneTypes[Phone] = True
            for Address in Contact.Addresses:
                AddressTypes[Address] = True
            for Email in Contact.EmailAddresses:
                EmailTypes[Email] = True
        with open(filename, 'w') as OutFile:
            OutFile.write('First Name\tLast Name')
            for Phone in PhoneTypes:
                OutFile.write('\t' + Phone + ' Phone')
            for Address in AddressTypes:
                OutFile.write('\t' + Address + ' Address')
            for Email in EmailTypes:
                OutFile.write('\t' + Email + ' Email')
            OutFile.write('\n')
            for Contact in self.VeryCoolDictionary.values():
                OutFile.write(Contact.FirstName + '\t' + Contact.LastName)
                for Phone in PhoneTypes:
                    if Contact.HasPhoneNumber(Phone):
                        OutFile.write('\t' + str(Contact.PhoneNumbers[Phone]))
                    else:
                        OutFile.write('\t')
                for Address in AddressTypes:
                    if Contact.HasAddress(Address):
                        OutFile.write('\t' + str(Contact.Addresses[Address]))
                    else:
                        OutFile.write('\t')
                for Email in EmailTypes:
                    if Contact.HasEmailAddress(Email):
                        OutFile.write('\t' + str(Contact.EmailAddresses[Email]))
                    else:
                        OutFile.write('\t')
                OutFile.write('\n')

                

if __name__ == '__main__':
    MyContacts = VeryCoolName()
    MyContacts.VeryCoolMenu()
