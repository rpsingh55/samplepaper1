l=list(map(int,input().split()))
print(l)
k=[]
for i in range(1,101):
     if i not in l:
        k.append(i)
print(*k,sep=',')
    

    
