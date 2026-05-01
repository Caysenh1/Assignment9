L1 = list(map(int,input("Enter numbers: ").split()))
L2 = list(map(int,input("Enter numbers: ").split()))
L1 = L1[::2]
L2 = L2[1::2]
print(*L1)
print(*L2)
L3 = L1 + L2
L3.sort()
for x in L3:
    print(x, end = " ")
