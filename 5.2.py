text = input()

a = text.count("a")
e = text.count("e")
i = text.count("i")
o = text.count("o")
u = text.count("u")

vowels = a + e + i + o + u
not_vowels = len(text) - vowels
print("Vowels:", vowels)
print("Not vowels:", not_vowels)

if (a == 0) and (e == 0) and (i == 0) and (o == 0) and (u == 0):
    print("False")
else:
    print(a, e, i, o, u)
