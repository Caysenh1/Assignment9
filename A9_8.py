N = int(input("Enter an interger: "))
i = N
H = 0
while True: 
    D = (i)**3
    i = i - 1
    H = D + H
    if i <= 0:
        print(H)
        break

    
    
    
