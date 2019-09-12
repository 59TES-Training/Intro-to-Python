palList= []

def palindrome(x, y):
    
    while y > 99:
        
        palin = x * y
        palin_for = str(palin)
        palin_bac = str(palin)[::-1]
        
        
        
        if palin_for == palin_bac:
            palList.append(palin)
            
        if x < 100:
            x = 999
            y -= 1
        else:    
            x -= 1
            print(palin_for, palin_bac, x, y)
            
    print(max(palList))
          
palindrome(999, 999)