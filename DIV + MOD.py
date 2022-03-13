from posixpath import split
m=0

t=int(input())
s=[]
for i in range(t):
    s.append(input())
for i in range(t):
    max=0
    l=s[i].split(" ")
    l0=int(l[0])
    l1=int(l[1])
    l2=int(l[2])
    if l2==1:
        print(l1)
        continue
    if l1%l2==l2-1:
        pass
    elif l1//l2>=1:
        m=l1
        l1 -=l1%l2 +1
        if l1 <l0:
            l1=m
    l1=l1//l2+l1%l2
    print(l1)
 