# DSP
this is a course in my university
import numpy as np
f=open('coindesk-bpi-USD-close.csv')
s=f.read()
sL=s.split('\n')
xL=[x.split(',')[-1]for x in sL]
yL=[float(x)for x in xL[1:-4]]
priceData=np.array(yL)
len(priceData)
<<2112
