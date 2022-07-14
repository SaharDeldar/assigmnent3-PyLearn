import random
t=int(input("enter a number:"))
arylist = []

while len(arylist)<t :
    rand=random.randint(0,t)
    if rand not in arylist:
        arylist.append(rand)
print(arylist)