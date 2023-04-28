x = int (1)
c = 'L'
for i in range(6):
    print(c)
    c = chr(ord(c)^x)
    x = x*2 + 1

