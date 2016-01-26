print("Enter Numerator>", end=' ')
A = int(input())
B = input("Enter Divisor> ")
B = int(B)
D = A // B
R = A % B
print("    %3d R%d"%(D,R))
print("   -----")
print("%3d|%3d"%(B,A))
F = A / B
print("Float = %g"%F)
