A = 0
B = 0
C = 0
B2 = 1
while True:
    A = int(input("Enter a number: "))
    if A == 0:
        break
    elif A == C:
        B += 1
        if B2 < B:
            B2 += 1
    else:
        B = 1
        C = A
    if A < B:
        A = B

print(f"The length of the largest sequence of equal numbers is: {B2}")

    
    
    
