l=list(map(int,input("Enter the numbers to find the factorial").split()))
import math
p=[]
for i in l:
    f=math.factorial(i)
    p.append(f)
print(p)



