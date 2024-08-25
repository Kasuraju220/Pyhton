num = int(input("Enter the num : "))
num_list = [[0 for x in range(num)] for y in range(num)]
low=0
high=num-1
count=int((num+1)/2)

for i in range(count):
    for j in range(low,high+1):
        num_list[i][j]=num
    for j in range(low+1,high+1):
        num_list[j][high]=num
    for j in range(high-1,low-1,-1):
        num_list[high][j]=num
    for j in range(high-1,low,-1):
        num_list[j][low]=num
    low=low+1
    hign =high-1
    num=num-1

for i in range(num):
    for j in range(num):
        print(num_list[i][j],end="\t")
    print()