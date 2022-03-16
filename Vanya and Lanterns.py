
def result(n):
    n=str(n)
    m=n.find(".")
    if m==-1:
        n+="."
        m=0
    for i in range(m,10):
        n+="0"
    return n
inp=input()
inp=inp.split(" ")
n=int(inp[0])
l=int(inp[1])
inp2=input()
inp2=inp2.split(" ")
inp2=[int(x) for x in inp2]
inp2.sort()
max=0
if inp2[0]>l-inp2[n-1]:
    max=inp2[0]*2
else:
    max=(l-inp2[n-1])*2
for i in range(n-1):
    """
    if i==0 and inp2[0]!=0:
        max=int(inp2[0])*2
        i_f=inp2[i]
        i_l=inp2[i+1]
    elif i==0:
        max=int(inp2[1])
        i_f=inp2[i]
        i_l=inp2[i+1]
    """
    if int(inp2[i+1])-int(inp2[i])>max:
        max=int(inp2[i+1])-int(inp2[i])
if n==1:
    if inp2[0]==0 or inp2[0]==l:
        max=l*2
    else:
        if inp2[0]>l-inp2[0]:
            max=inp2[0]*2
        else:
            max=(l-inp2[0])*2
if l-int(inp2[n-1])>max/2 and n!=1:
    if n==2:
        if int(inp2[1])-int(inp2[0])>0:
            max=(l-int(inp2[n-1]))*2

print(result(max/(2)))