L = []
for i in range(26):
    y=(4*i+3)%27
    if y == i:
        L.append(i)

print(L)