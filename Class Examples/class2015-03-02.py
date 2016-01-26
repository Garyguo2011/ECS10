
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

    
    def __init__(self):
        self.AreaCode = 530
        self.Prefix = 752
        self.Suffix = 1

    def __str__(self):
        return '(%d) %d-%04d'%(self.AreaCode,self.Prefix,self.Suffix)

    def IsValid(phonenumber_as_string):
        if type(phonenumber_as_string) != str:
            return False
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

    def __init__(self):
        self.Street1 = 'One Shields Ave.'
        self.Street2 = '2063 Kemper Hall'
        self.City = 'Davis'
        self.State = 'CA'
        self.ZipCode = 95616
        self.ZipPlus4 = -1

    def __str__(self):
        ReturnString = self.Street1 + '\n'
        if self.Street2 != '':
            ReturnString += self.Street2 + '\n'
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
    def __init__(self):
        self.Address = 'cjnitta@ucdavis.edu'

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

if __name__ == '__main__':
##    TempNumber = input("Enter Number> ")
##    NewPhoneNumber = PhoneNumber()
##    NewPhoneNumber.Parse(TempNumber)
##    print(str(NewPhoneNumber))
##    NewAddress = Address()
##    TempString = input("Enter Address> ")
##    print(NewAddress.Parse(TempString))
##    print(str(NewAddress))
    TempString = input("Enter Address> ")
    print(EmailAddress.IsValid(TempString))
    
