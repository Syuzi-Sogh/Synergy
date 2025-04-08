n = int(input())
counter = 0

for i in range(n):
    if (i == 0):
        i += 1
    if (n % i == 0):
        counter += 1

print(counter)