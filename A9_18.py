N = int(input("Enter a number: "))
fib = 1
fib2 = 1
fib3 = 1
L = []
for i in range(N+2):
    fib2 = fib
    fib = fib3
    fib3 = fib + fib2
    L.append(fib)
    if len(L) > N:
        break
if N not in L:
    print("Not a Fibonacci number")
else:
    print(L.index(N)+2)

    
