N = int(input("E: "))
var1 = 1
total1 = 0
totale = 0
for i in range(1, N+1):
    totale = total1 + totale
    total1 = var1*var1
    var1 += 1
print(totale)
    
