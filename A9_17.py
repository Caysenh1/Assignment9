N = int(input("Enter a number: "))
L = []
Card = []
miss = N
for i in range(N-1):
    Card = int(input("Enter card: "))
    L.append(Card)
    miss = N 
    if miss in L:
        miss = miss - 1
        continue
print(miss)
    
    

