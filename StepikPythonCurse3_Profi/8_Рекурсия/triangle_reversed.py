def triangle(h):
    if h <= 0:
        return
    triangle(h-1)
    print('*'*h)
        
        
        
    
triangle(3)