x=input()
x=int(x)
n=0
if x>=100:
    rem=x%100
    n +=(x-rem)/100
    x=rem
if x>=20:
    rem=x%20
    n +=(x-rem)/20
    x=rem
if x>=10:
    rem=x%10
    n +=(x-rem)/10
    x=rem
if x>=5:
    rem=x%5
    n +=(x-rem)/5
    x=rem
if x>=1:
    rem=x%1
    n +=(x-rem)/1
    x=rem
print(int(n))

