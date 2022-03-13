for i in range(int(input())):
    s=input()
    c=input()
    n=0
    for j in range(0,len(s),2):
        if s[j]==c:
            print("YES")
            n=1
            break
    if n==0:
        print("NO")    