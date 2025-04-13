import random

def pl(x):
    for i in x:
        print(i)

n = int(input())

matrix1 = [[0 for x in range(n)] for y in range(n)]

for i in range(n):
    for j in range(n):
        matrix1[i][j] = random.random()

print(matrix1)
matrix2 = [[0 for x in range(n)] for y in range(n)]

for i in range(n):
    for j in range(n):
        matrix2[i][j] = random.randint(0, 100)

print(matrix2)

matrix3 = [[0 for x in range(n)] for y in range(n)]

for i in range(n):
    for j in range(n):
        matrix3[i][j] = matrix1[i][j] + matrix2[i][j]

pl(matrix3)