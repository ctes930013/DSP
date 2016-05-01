# DSP
this is a course in my university


1.

import numpy as np

f=open('coindesk-bpi-USD-close.csv')

s=f.read()

sL=s.split('\n')

xL=[x.split(',')[-1]for x in sL]

yL=[float(x)for x in xL[1:-4]]

priceData=np.array(yL)

len(priceData)

<<2112

2.

import numpy as np

import pylab as pl

def movingAverage(x,length):
    y=np.convolve(x,np.ones(length)/length)
    y=y[:len(x)]
    return y

pl.plot(priceData)

ma100=movingAverage(priceData,100)

pl.plot(ma100)

ma500=movingAverage(priceData,500)

pl.plot(ma500)

ma1000=movingAverage(priceData,1000)

pl.plot(ma1000)
