def deltaHSI (colour1: tuple[int | float, int | float, int | float], 
              colour2: tuple[int | float, int | float, int | float]
              ) -> float: 
    """
    Calculates the delta (difference) between two HSI color values.
    
    Args:
        colour1 (tuple[int | float, int | float, int | float]): The first HSI color value.
        colour2 (tuple[int | float, int | float, int | float]): The second HSI color value.
    
    Returns:
        float: The delta (difference) between the two HSI color values.
        
    Example:
        eltaHSI((210, 33.3, 150), (139, 57.1, 117))
        81.45
    """
        
    from math import cos, pi, sqrt
    
    (H1, S1, I1) = colour1
    (H2, S2, I2) = colour2
    
    delta_I: int | float = abs(I1 - I2)
    
    if abs(H1 - H2) <= pi:
        t: int | float = abs(H1 - H2)
    else:
        t: float = 2 * pi - abs(H1 - H2)
    
    delta_C: float = sqrt( S1**2 + S2**2 - (2 * S1 * S2 * cos(t)) )
    
    delta_HSI: float = sqrt(delta_I**2 + delta_C**2)
    
    return delta_HSI
