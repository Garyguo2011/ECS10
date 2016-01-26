
from caesar import *
import inspect
import random
import os

if 'CaesarCipher' not in globals():
    print('Error: Class CaesarCipher not defined!')
    exit(0)    

if not inspect.isclass(CaesarCipher):
    print('Error: CaesarCipher is not a class!')
    exit(0)    

try:
    MyCaesarCipher = CaesarCipher()
except:
    print('Error: Failed to create instances of CaesarCipher!')
    exit(0) 
Functions = []
Functions.append(('ClearAll',1))   
Functions.append(('LoadEncryptedFile',2))
Functions.append(('LoadDecryptedFile',2))
Functions.append(('SaveEncryptedFile',2))
Functions.append(('SaveDecryptedFile',2))
Functions.append(('PrintEncrypted',1))
Functions.append(('PrintDecrypted',1))
Functions.append(('Encrypt',2))
Functions.append(('Decrypt',2))

for Function in Functions:
    if not hasattr(MyCaesarCipher,Function[0]):
        print('Error: CaesarCipher is missing %s function!'%Function[0])
        exit(0)    
    FunctionPointer = getattr(MyCaesarCipher, Function[0], None)
    if not callable(FunctionPointer):
        print('Error: CaesarCipher attribute %s is not a function!'%Function[0])
        exit(0)  
    ArgSpec = inspect.getargspec(FunctionPointer)
    if len(ArgSpec.args) != Function[1]:
        print('Error: CaesarCipher function %s takes %d parameters, but should take %d!'%(Function[0],len(ArgSpec.args),Function[1]))
        exit(0) 
    if ArgSpec.args[0] != 'self':
        print('Error: First argument to CaesarCipher function %s is %s, but should be self!'%(Function[0],ArgSpec.args[0]))
        exit(0)
    
DecryptedFilename = 'decrypted_%d.txt'%random.randint(1,1000)
EncryptedFilename = 'encrypted_%d.txt'%random.randint(1,1000)
PossibleShifts = []
for Shift in range(1, 62):
    if Shift != 26 and Shift != 36:
        PossibleShifts.append(Shift)
SelectedShift = PossibleShifts[random.randint(0,len(PossibleShifts)-1)]
try:
    if False != MyCaesarCipher.SaveEncryptedFile(EncryptedFilename):
        print('Error: CaesarCipher function SaveEncryptedFile did not return False when empty text!')
        exit(0)
    if False != MyCaesarCipher.SaveDecryptedFile(DecryptedFilename):
        print('Error: CaesarCipher function SaveDecryptedFile did not return False when empty text!')
        exit(0)
    with open(DecryptedFilename,'w') as OutFile:
        for Char in range(32, 127):
            OutFile.write(chr(Char))
    MyCaesarCipher.LoadDecryptedFile(DecryptedFilename)
    MyCaesarCipher.Encrypt(SelectedShift)
    if True != MyCaesarCipher.SaveEncryptedFile(EncryptedFilename):
        print('Error: CaesarCipher function SaveEncryptedFile did not return True when saving encrypted text!')
        if os.path.isfile(DecryptedFilename):
            os.remove(DecryptedFilename)
        exit(0)
    if not os.path.isfile(EncryptedFilename):
        print('Error: CaesarCipher function SaveEncryptedFile did not save file!')
        if os.path.isfile(DecryptedFilename):
            os.remove(DecryptedFilename)
        exit(0)
    MyCaesarCipher.ClearAll()
    with open(EncryptedFilename) as InFile:
        InText = InFile.read()
        Index = 0
        for ASCII in range(32, 127):
            UChar = chr(ASCII)
            if ('0' <= UChar <= '9') or ('A' <= UChar <= 'Z') or ('a' <= UChar <= 'z'):
                ExpectedChar = UChar
                for CurShift in range(SelectedShift):
                    if ExpectedChar == '9':
                        ExpectedChar = 'A'
                    elif ExpectedChar == 'Z':
                        ExpectedChar = 'a'
                    elif ExpectedChar == 'z':
                        ExpectedChar = '0'
                    else:
                        ExpectedChar = chr(ord(ExpectedChar) + 1)
                if ExpectedChar != InText[Index]:
                    print('Error: CaesarCipher encrypted a character wrong!')
                    raise Exception
            else:
                if InText[Index] != UChar:
                    print('Error: CaesarCipher encrypted a character that should not be encrypted!')
                    raise Exception
            Index += 1
    MyCaesarCipher.LoadEncryptedFile(EncryptedFilename)
    MyCaesarCipher.Decrypt(SelectedShift)  
    if os.path.isfile(DecryptedFilename):
        os.remove(DecryptedFilename)    
    if True != MyCaesarCipher.SaveDecryptedFile(DecryptedFilename):
        print('Error: CaesarCipher function SaveDecryptedFile did not return True when saving decrypted text!')
        if os.path.isfile(DecryptedFilename):
            os.remove(DecryptedFilename)
        if os.path.isfile(EncryptedFilename):
            os.remove(EncryptedFilename)
        exit(0)
    with open(DecryptedFilename) as InFile:
        InText = InFile.read()
        CompareText = ''
        for ASCII in range(32, 127):
            CompareText += chr(ASCII)
        if InText != CompareText:
            print('Error: CaesarCipher decrypted file did not match expected text!')
            raise Exception
            
except:
    print('Error: CaesarCipher threw an unexpected exception!')
    if os.path.isfile(DecryptedFilename):
        os.remove(DecryptedFilename)
    if os.path.isfile(EncryptedFilename):
        os.remove(EncryptedFilename)
    raise
if os.path.isfile(DecryptedFilename):
    os.remove(DecryptedFilename)
if os.path.isfile(EncryptedFilename):
    os.remove(EncryptedFilename)
print('No Errors Detected!')
