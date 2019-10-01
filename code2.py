n = 5
for k in range(n):
    for i in range(k+1):
        line = 1
        if (i>k-i):
            i = k-i
        for j in range(i):
            line = line * (k-j)
            line = line //(j+1)
        print(line,'',end='')
    print()
