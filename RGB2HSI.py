def RGB2HSI (colour: tuple[int | float, int | float, int | float]) -> tuple[int, float, int]:
    """
    Converts an RGB color tuple to an HSI (Hue, Saturation, Intensity) tuple.
    
    Args:
        colour (tuple[int | float, int | float, int | float]): A tuple of RGB color values.
    
    Returns:
        tuple[int, float, int]: A tuple containing the Hue (0-360), Saturation (0-100), and Intensity (0-255) values.
        
    Examples:
        RGB2HSI((100, 150, 200))
        (210, 33.3, 150)
    """
    
    from math import acos, pi, sqrt
    
    (R, G, B) = colour
       
    r: float = R / ((R + 0.000001) + (G + 0.000001) + (B + 0.000001)) 
    g: float = G / ((R + 0.000001) + (G + 0.000001) + (B + 0.000001))
    b: float = B / ((R + 0.000001) + (G + 0.000001) + (B + 0.000001))
   
    num: float = 0.5 * ((r - g) + (r - b))
    den: float = sqrt((r - g)**2 + (r - b) * (g - b))
    h: float = acos(num / (den + 0.0000001))
    
    if b <= g:
        h: float = h
    else:
        h: float = 2 * pi - h
    
    H: int = round(h * 180/pi)
    
    S: float = round(100 * (1 - 3 * min(r, g, b) + 0.000001), 1)
    
    I: int = round((R + G + B)/3)
         
    return (H, S, I)
