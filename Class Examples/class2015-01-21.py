LineInput = 'P'
while LineInput[0] != 'Q':
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
        ## begins comment
        DecodedString = ''
        LastWasEscape = False
        for Char in EncodedLine:
            if LastWasEscape:
                if Char == '\\':
                    DecodedString = DecodedString + '\\'
                elif Char == 'n':
                    DecodedString = DecodedString + '\n'
                elif Char == 'r':
                    DecodedString = DecodedString + '\r'
                elif Char == 't':
                    DecodedString = DecodedString + '\t'
                elif Char == 'a':
                    DecodedString = DecodedString + '\a'
                else:
                    DecodedString = DecodedString + Char
                LastWasEscape = False
            elif Char == '\\':
                LastWasEscape = True
            elif Char == '#':
                break
            else:
                LastWasEscape = False
                DecodedString = DecodedString + Char
            
        print('DecodedString ="%s"'%DecodedString)                                       
    elif LineInput.find('L') == 0:
        print('LaTeX encoding')
        IndexOfSpace = LineInput.find(' ')
        if IndexOfSpace >= 0:
            EncodedLine = LineInput[IndexOfSpace:].strip()
        else:
            EncodedLine = input('Please input LaTeX encoded line> ').strip()
        print('EncodedLine ="%s"'%EncodedLine)
        #`` => "
        #'' => "
        #\\{ => {
        #\\} => }
        #\\% => %
        #% begins comment
        DecodedString = ''
        LastWasEscape = False
        LastWasBackQuote = False
        LastWasApos = False
        for Char in EncodedLine:
            if LastWasEscape:
                if Char == '\\':
                    DecodedString = DecodedString + '\\'
                elif Char == '{':
                    DecodedString = DecodedString + '{'
                elif Char == '}':
                    DecodedString = DecodedString + '}'
                elif Char == '%':
                    DecodedString = DecodedString + '%'
                else:
                    DecodedString = DecodedString + Char
                LastWasEscape = False
            elif LastWasBackQuote:
                if Char == '`':
                    DecodedString = DecodedString + '"'
                else:
                    DecodedString = DecodedString + '`' + Char
                LastWasBackQuote = False
            elif LastWasApos:
                if Char == '\'':
                    DecodedString = DecodedString + '"'
                else:
                    DecodedString = DecodedString + "'" + Char
                LastWasApos = False
            elif Char == '\\':
                LastWasEscape = True
            elif Char == '`':
                LastWasBackQuote = True
            elif Char == '\'':
                LastWasApos = True
            elif Char == '%':
                break
            else:
                LastWasEscape = False
                DecodedString = DecodedString + Char
        print('DecodedString ="%s"'%DecodedString)  
    else:
        print('Unknown encoding')    
