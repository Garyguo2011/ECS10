import math

X = float(input('Enter X>'))
Y = float(input('Enter Y>'))
Point1 = (X, Y)
X = float(input('Enter X>'))
Y = float(input('Enter Y>'))
Point2 = (X, Y)
DistanceX = Point2[0] - Point1[0]
DistanceY = Point2[1] - Point1[1]
DistanceSquared = DistanceX * DistanceX + DistanceY**2

print("Distance from",Point1,"to",Point2,"is",DistanceSquared**0.5)
print("Distance from",Point1,"to",Point2,"is",math.sqrt(DistanceSquared))

A = int(input("Enter number>"))
B = int(input("Enter other >"))
AList = []
AList.append(A)
AList.append(B)
Length = len(str(max(AList)))
print("",max(AList))
MinLength = len(str(min(AList)))
Spaces = ' '*(Length-MinLength)
print("-%s%d"%(Spaces,min(AList)))
print('-'*(Length+1))
Delta = max(AList)-min(AList)
Spaces = ' '*(Length - len(str(Delta)))
print(Spaces,Delta)
