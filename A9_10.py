N = int(input("Enter a number: "))
D = []
L = []
while N > 0:
    D = int(input("Enter: "))
    L.append(D)
    N = N - 1
    if N <= 0:
        print(L.count(0))
        break
    
    
    

