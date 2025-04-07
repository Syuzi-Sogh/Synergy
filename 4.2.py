inPut = int(input())
pow_ = inPut % 10
inPut = inPut // 10
base = inPut % 10
result = base ** pow_
inPut = inPut // 10
multiplier = inPut % 10
result = result * multiplier
inPut = inPut // 10
a = inPut % 10
inPut = inPut // 10
result1 = inPut - a
result = result // result1
print(result)