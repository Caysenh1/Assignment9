N = []
while True:
    X = int(input("Enter a number: "))
    if X == 0:
        break
    if X % 2 == 0:
        N.append(X)
print(len(N))
    
