l = [3e-03,'The',True,66]
t = (5.21,'JIIT',False,454)
for i in range(len(l)):
    if l[i]:
        l[i] = l[i] + t[i]
    else:
        t[i] = l[i] + t[i]
        break
print(l,t)
