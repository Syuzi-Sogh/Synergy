min_cost = int(input())
Mike_money = int(input())
Ivan_money = int(input())

if (Mike_money >= min_cost) and (Ivan_money >= min_cost):
    print("2")
elif (Mike_money >= min_cost) and (Ivan_money < min_cost):
    print("Mike")
elif (Mike_money < min_cost) and (Ivan_money >= min_cost):
    print("Ivan")
elif (Mike_money < min_cost) and (Ivan_money < min_cost) and (Mike_money + Ivan_money == min_cost):
    print("1")
else:
    print("0")