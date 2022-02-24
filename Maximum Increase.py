x=int(input())
s1=input()
arr_sequence=s1.split(" ")
n=1
max=1
for i in range(x-1):
    if int(arr_sequence[i])<int(arr_sequence[i+1]):
        n+=1
    else:
        n=1
    if n>max:
        max=n
print(max)