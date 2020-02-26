s1=input("Enter the string")
s2=input("Enter the substring")
c=0
for i in range(len(s1)):
     if s1[i:i+len(s2)]==s2:
        c+=1
print(c)
