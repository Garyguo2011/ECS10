import operator
def Function(a, b):
    print('a = %s, b = %s'%(a,b))
    return a + b


X = Function(5, 6)

print(X)

Y = Function(Function('Hello','World'),Function('Bye','.'))
print(Y)

InputString = input('Enter a b> ')
InputList = InputString.split()
A = InputList[0]
B = InputList[1]
print(A, B)

def PrintMenu():
    print('A Apple')
    print('O Orange')
    print('--------')
    return

PrintMenu()

MyGlobal = [6]

def MyFunction(parameter):
    #MyGlobal[0] = 8
    print(' Parameter',parameter[0])
    parameter[0] = 7
    MyLocal = 7
    print(' Parameter',parameter[0])
    print(' MyGlobal',MyGlobal[0])

print('MyGlobal',MyGlobal[0])
MyFunction(MyGlobal[:])
print('MyGlobal',MyGlobal[0])
if len(MyGlobal):
    pass
else:
    print('Else')

def MultiParam(a=4,b=6,c=9):
    print(a,b,c)

MultiParam(b=99,a=-4)

MyList = [('a',5),('b',3),('c',2),('d',36),('e',8),('f',90),('g',32)]
print(MyList)
MyList.sort(key=itemgetter(1))
print(MyList)


