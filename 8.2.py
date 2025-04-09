size = int(input())
ls = list(map(int, input().split()))
ls1 = []
ls2 = ls[-1]

for i in range(len(ls) - 1):
    ls1.append(ls[i])

ls1.insert(0, ls2)
print(*ls1)