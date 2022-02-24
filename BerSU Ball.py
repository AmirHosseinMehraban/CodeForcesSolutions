boy_number=int(input())
boy_sequence=input()
arr_boy=boy_sequence.split(" ")
girl_number=int(input())
girl_sequence=input()
arr_girl=girl_sequence.split(" ")
arr_boy = [int(i) for i in arr_boy]
arr_boy.sort()
arr_girl = [int(i) for i in arr_girl]
arr_girl.sort()
count=0
for i in range(boy_number):
    for j in range(girl_number):
        if abs(int(arr_boy[i]) - int(arr_girl[j]))<2:
            count+=1
            arr_girl[j]="102"
            break
print(count)