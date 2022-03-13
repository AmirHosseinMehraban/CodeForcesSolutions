def divisior(n):
    x=[]
    for i in range(2,n+1):
        if n%i==0:
            x.append(i)
    return x
t=int(input())
l1=[]
n=0
for i in range(t):
    l1.append(int(input()))
for i in range(t):
    l2=divisior(l1[i])
    for j in range(len(divisior(l1[i]))):
        if l2[j]%2 !=0:
            n+=1
        if n>1:
            break
    if n==1:
        print("YES")
    else:
        print("NO")
    n=0
        
