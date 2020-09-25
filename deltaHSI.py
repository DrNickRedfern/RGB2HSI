#!/usr/bin/env python
# coding: utf-8

# In[1]:


def deltaHSI (colour1, colour2): # inputs are tuples of HSI colour values
    
    from math import cos, pi, sqrt
    
    (H1, S1, I1) = colour1
    (H2, S2, I2) = colour2
    
    delta_I = abs(I1 - I2)
    
    if abs(H1 - H2) <= pi:
        t = abs(H1 - H2)
    else:
        t = 2 * pi - abs(H1 - H2)
    
    delta_C = sqrt( S1**2 + S2**2 - (2 * S1 * S2 * cos(t)) )
    
    delta_HSI = sqrt(delta_I**2 + delta_C**2)
    
    return delta_HSI

