ListOfCalls = []

def Function1():
    print(' ')
    print('Function 1',ListOfCalls)
    ListOfCalls.append('Function1')
    while True:
        print(' ')
        print('Item 1')
        print('Item 2')
        print('Item 3')
        print('Item 4')
        print('Done D')
        InputValue = ''
        while InputValue not in ['1','2','3','4','D']:
            InputValue = input('Enter Selection> ').strip().upper()

        if InputValue == '1':
            Function1()
        elif InputValue == '2':
            Function2()
        elif InputValue == '3':
            Function3()
        elif InputValue == '4':
            Function4()
        elif InputValue == 'D':
            ListOfCalls.pop(-1)
            return 
    

def Function2():
    print(' ')
    print('Function 2',ListOfCalls)
    ListOfCalls.append('Function2')
    Mapping = {}
    for Index, FunctionName in enumerate(ListOfCalls):
        print(Index+1,FunctionName)
        Mapping[Index+1] = FunctionName
    InputValue = 0
    while InputValue not in Mapping:
        InputValue = input("Enter a Choice> ").strip()
        if InputValue.isnumeric():
            InputValue = int(InputValue)
    Function3(Mapping[InputValue])
    ListOfCalls.pop(-1)

def Function3(item='None'):
    print(' ')
    print('Function 3',ListOfCalls)
    ListOfCalls.append('Function3')
    print(item)
    ListOfCalls.pop(-1)
    
def Function4():
    print(' ')
    print('Function 4',ListOfCalls)
    ListOfCalls.append('Function4')
    for Index,Item in enumerate(ListOfCalls):
        if 0 > Item.find('Function'):
            NameToPrint = Item
        else:
            NameToPrint = Item + ' x' + Item[-1]
        print('%d. %-16s @ $%4.2f : $%8.2f'%(Index+1,NameToPrint,Index,Index*Index))
    ListOfCalls.pop(-1)

def MainMenu():
    
    print('Main Menu',ListOfCalls)
    ListOfCalls.append('MainMenu')

    while True:
        print(' ')
        print('Item 1')
        print('Item 2')
        print('Item 3')
        print('Item 4')
        print('Quit Q')

        InputValue = ''
        while InputValue not in ['1','2','3','4','Q']:
            InputValue = input('Enter Selection> ').strip().upper()

        if InputValue == '1':
            Function1()
        elif InputValue == '2':
            Function2()
        elif InputValue == '3':
            Function3()
        elif InputValue == '4':
            Function4()
        elif InputValue == 'Q':
            return
            

    



MainMenu()
