# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
MyTriangleSignal

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 13:45:20 2016

@author: csie3
"""

from thinkdsp import *


class RyTriangleSignal01(Sinusoid):
    """Represents a triangle signal."""
    
    def evaluate(self, ts):
        """Evaluates the signal at the given times.

         ts: float array of times
        
        returns: float wave array
        """
        
        ts = np.asarray(ts)

        T= 1/self.freq
        
        y0= T/2
        
        ys = abs((ts % T) - y0) / y0
                 

        return ys        




class MyTriangleSignal(Sinusoid):
    """Represents a triangle signal."""
    
    def evaluate(self, ts):
        """Evaluates the signal at the given times.

        ts: float array of times
        
        returns: float wave array
        """      
        '''
        ts = np.asarray(ts)
        cycles = self.freq * ts + self.offset / PI2
        frac, _ = np.modf(cycles)
        ys = np.abs(frac - 0.5)
        ys = normalize(unbias(ys), self.amp)
        return ys
        '''
        #T= 1/200
        T= 1/self.freq
        xL= []       
        for t in ts:           
            t= t % T  # also good for real number
            #
            #  0<= t <= T/2
            #
            if t>=0 and t< T/2: 
                x= -4/T * t + 1            
            #
            #  T/2 <= t <= T
            #
            elif t>=T/2 and t<T:  
                x= +4/T * t - 3            
            xL = xL + [x]
        ys= np.asarray(xL)        
        return ys
