
arry_list=[]
messages=""
while True:
    numbers=input("enter anumber or write end:")
    if numbers=="end":
        break
    else:
        arry_list.append(int(numbers))
    min=arry_list[0]
print(arry_list)

for i in range(1,len(arry_list)):
    if min>arry_list[i]:
        messages="It is not sorted from smallest to largest"
        print(messages)
        break
    else:
        min=arry_list[i]
if messages=="":
    print("It is arranged from small to large")
