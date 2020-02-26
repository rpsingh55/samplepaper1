D=list(map(int,input().split(',')))
C=50
H=30
t=[]
for i in D:
     Q=((2*C*i)/H)**0.5
     t.append(int(Q))
print(t)

