def RGB2HSI ( colour ): # input is a tuple of RGB colour values, e.g. (100, 200, 150)
    
    from math import acos, pi, sqrt
    
    (R, G, B) = colour
       
    r = R / ((R + 0.000001) + (G + 0.000001) + (B + 0.000001)) 
    g = G / ((R + 0.000001) + (G + 0.000001) + (B + 0.000001))
    b = B / ((R + 0.000001) + (G + 0.000001) + (B + 0.000001))
   
    num = 0.5 * ((r - g) + (r - b))
    den = sqrt((r - g)**2 + (r - b) * (g - b))
    h = acos(num / (den + 0.0000001))
    
    if b <= g:
        h = h
    else:
        h = 2 * pi - h
    
    H = round(h * 180/pi)
    
    S = round(100 * (1 - 3 * min(r, g, b) + 0.000001), 1)
    
    I = round((R + G + B)/3)
         
    return (H, S, I)

