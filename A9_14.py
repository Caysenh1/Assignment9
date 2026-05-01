N = int(input("Enter a number: "))
for i in range(2, N):
    if i%2 == 0 or i%3 == 0:
        print(i)
        i+=1
