N = int(input("Enter a number: "))
for i in range(2,N):
    for x in range(2,i):
        if i%x == 0:
            break
    else:
        print(i)
        
        
        
   
    
    
    
    
    
