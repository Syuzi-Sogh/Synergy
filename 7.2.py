tmp = 'a  b  c  d e'

for i in range(0, len(tmp)):
    if tmp[i] == ' ' and tmp[i + 1] == ' ':
        print(tmp.split(' '), end=' ')
        break