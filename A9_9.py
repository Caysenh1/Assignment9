x = float(input("Enter miles ran: "))
y = float(input("Enter miles you need to run: "))
D = 1
while x <= y:
    x = x + x*0.1
    D = D + 1
    if x >= y:
        print(D)
        break
    
