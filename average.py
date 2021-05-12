import cv2
import numpy as np

def averagePixels( array ):
    
    def avg(array):
        count, summation = 0.0, 0.0
        for row in array:
            for coloumn in row:
                count += 1
                summation += coloumn
        
        average =  summation // count
        return int( average )
    
    b , g , r = cv2.split( array )
    b , g , r = avg(b), avg(g), avg(r)
    
    return f'{b},{g},{r}'