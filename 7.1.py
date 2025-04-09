temp = input()
mid = len(temp) // 2
smth = 0

for i in range(0, mid):
    for j in range(mid, len(temp)):
        if temp[j] == temp[i]:
            smth = 1

if (smth == 1):
    print("Yes")
else :
    print("No")