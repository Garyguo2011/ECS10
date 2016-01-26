LineInput = input('P = python, L = LaTeX followed by string> ')
#print('LineInput = "%s"'%LineInput)
LineInput = LineInput.strip()
#print('LineInput = "%s"'%LineInput)
if LineInput.find('P') == 0:
    print('Python encoding')
    IndexOfSpace = LineInput.find(' ')
    if IndexOfSpace >= 0:
        EncodedLine = LineInput[IndexOfSpace:].strip()
    else:
        EncodedLine = input('Please input python encoded line> ').strip()
    print('EncodedLine ="%s"'%EncodedLine)
    #\\ => \
    #\n => newline
    #\r => carriage return
    #\t => tab
    #\a => audible

    DecodedString = EncodedLine.replace('\\\\','~')
    DecodedString = DecodedString.replace('\\n','\n')
    DecodedString = DecodedString.replace('\\r','\r')
    DecodedString = DecodedString.replace('\\t','\t')
    DecodedString = DecodedString.replace('\\a','\a')
    DecodedString = DecodedString.replace('~','\\')
    print('DecodedString ="%s"'%DecodedString)                                       
elif LineInput.find('L') == 0:
    print('LaTeX encoding')
    IndexOfSpace = LineInput.find(' ')
    if IndexOfSpace >= 0:
        EncodedLine = LineInput[IndexOfSpace:].strip()
    else:
        EncodedLine = input('Please input LaTeX encoded line> ').strip()
    print('EncodedLine ="%s"'%EncodedLine)
    DecodedString = EncodedLine.replace('\\%','~')
    IndexOfPercent = DecodedString.find('%')
    if IndexOfPercent >= 0:
        DecodedString = DecodedString[:IndexOfPercent ]
    DecodedString = DecodedString.replace('~','%')
    print('DecodedString ="%s"'%DecodedString)  
else:
    print('Unknown encoding')    
