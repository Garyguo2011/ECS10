
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
        self.ZipCode = '95616'
        self.Country = 'USA'



if __name__ == '__main__':
    TempNumber = input("Enter Number> ")
    NewPhoneNumber = PhoneNumber()
    NewPhoneNumber.Parse(TempNumber)
    print(str(NewPhoneNumber))
