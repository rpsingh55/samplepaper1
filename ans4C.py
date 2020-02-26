s=input("enter the sentence")
k=s.lower()
t=[]
for i in k:
    if i not in t and i.isalpha():
       t.append(i)

if len(t)==26:
    print("Pangram")
else:
    print("Not pangram")

