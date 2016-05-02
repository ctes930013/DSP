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

<<請打開 signal01.png

ma100=movingAverage(priceData,100)

pl.plot(ma100)

<<請打開 signal02.png

ma500=movingAverage(priceData,500)

pl.plot(ma500)

<<請打開 signal03.png

ma1000=movingAverage(priceData,1000)

pl.plot(ma1000)

<<請打開 signal04.png

3.

print(priceData[1000:1005])

<<[ 93.      90.      82.386   68.3557  93.07  ]

print(ma100[1000:1005])

<<[ 48.094242  48.859242  49.548702  50.097719  50.892543]

 print(ma500[1000:1005])
 
<<[ 15.982646   16.156526   16.3150678  16.4461912  16.626675 ]

print(ma1000[1000:1005])

<<[  9.9662261  10.0561453  10.1384566  10.2067331  10.2997526]

4.



5.

from thinkdsp import*

pNoise=PinkNoise()

pNoise.make_wave(2112).play()

rNoise=BrownianNoise()

rNoise.make_wave(2112).play()

wNoise=UncorrelatedUniformNoise()

wNoise.make_wave(2112).play()

6.

 pNoise.make_wave(2112).plot()
 
 <<請打開 signal05.png
 
 rNoise.make_wave(2112).plot()
 
 <<請打開 signal06.png
 
 wNoise.make_wave(2112).plot()
