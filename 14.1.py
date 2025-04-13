def rec(ls1):
    if len(ls1) <= 0:
        print(end='\n'"Конец списка")
        return
    print(ls1[0], end=' ')
    ls1.pop(0)
    rec(ls1)


ls = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
rec(ls)