def Exponential(val,exponent):
    if exponent == 0:
        return 1
    return val * Exponential(val,exponent-1)


print(Exponential(2,6))

class CDPlayer:
    def __init__(self):
        pass

    def PlayCD(self):
        
        print('Play CD')


class DVDPlayer(CDPlayer):
    def __init__(self):
        CDPlayer.__init__(self)

    def PlayDVD(self):
        print('Play DVD')

class BlurayPlayer(DVDPlayer):
    def __init__(self):
        DVDPlayer.__init__(self)

    def PlayBluray(self):
        print('Play Bluray')



MyBluray = BlurayPlayer()

MyBluray.PlayCD()
MyBluray.PlayDVD()
MyBluray.PlayBluray()

def Not10(val):
    if val != 10:
        raise Exception

MyRange = int(input('Enter a number> '))
try:
    Not10(MyRange)
    for I in range(MyRange):
        if I < 5:
            print(I)
            if I > 2:
                continue
        else:
            break
        print('.')
    else:
        print("Else")

except:
    print("Exception!")
MyDict = {1:2}
print(list(MyDict.keys()))
