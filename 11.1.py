def f(n):
    if n == 0:
        return 1

    res = 1
    for i in range(n + 1):
        if i == 0:
            i += 1
        res = res * i
    return res

def result(number):
    ls = []
    for i in range(f(number), 0, -1):
        ls.append(f(i))
    print(ls)

number = int(input())
result(number)