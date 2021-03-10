

# non -parametric sign test for sinle samall sample
import numpy as np
import pandas as pd
from scipy.stats import binom
x=np.array([119,120,125,122,118,117,126,114,115,123,121,120,124,127,126])
M=120
differ=x-M      # difference array
T1=sum(x>M)     #No of positive sign
A=(x>M)
T2=sum(x<M)     # No of negative sign
B=(x<M)
T=min(T1,T2)    # No of fever sign
N=T1+T2
P=binom.cdf(T,N,0.5)
D=pd.DataFrame({'Sample(x)':x,'Differnce':differ,'- sign':A,'+ sign':B})
print(D)   #    gives data frame
print('P_value=%.3f'%(P))
alpha= 0.05
print('Level_of_significance=%.3f'%(alpha))
if P>alpha:
    print('Accept Ho at 5% level of significance')
    print ('RESULT:-120 is population median of give sample x')
else:
    print('reject Ho at 5% level of significance')
    print ('RESULT:-120 is not population median of give sample x')




 # non -parametric sign test for Two samall sample

x=np.array([70,69,72,74,66,68,69,70,71,69,73,72,68,72,67])
y=np.array([69,72,71,74,68,67,72,72,72,70,75,73,71,72,69])
d=x-y     # difference array
T1=sum(d>0)     #No of positive sign
A=(d>0)
T2=sum(d<0)     # No of negative sign
B=(d<0)
T=min(T1,T2)    # No of fever sign
N=T1+T2
P=binom.cdf(T,N,0.5)
D=pd.DataFrame({'Sample1(x)':x,'Sample2(y)':y,'Differnce':d,'- sign':A,'+ sign':B})
print(D)   #    gives data frame
print('p_value=%.3f'%(P))
alpha= 0.05
print('Level_of_significance=%.3f'%(alpha))
if P>alpha:
    print('Accept Ho at 5% level of significance')
    print ('RESULT:-Population median of both sample are same')
else:
    print('reject Ho at 5% level of significance')
    print ('RESULT:-Population median of both sample are different')


# non -parametric sign test for sinle large  sample n>20

x=np.array([119,120,125,122,118,117,126,114,115,123,121,120,124,127,126])
M=120
differ=x-M      # difference array
T1=sum(x>M)     #No of positive sign
A=(x>M)
T2=sum(x<M)     # No of negative sign
B=(x<M)
T=min(T1,T2)    # No of fever sign
N=len(x)
mu=N/2
sigma=np.sqrt(N/4)
calZ=np.abs((T-mu)/sigma)
D=pd.DataFrame({'Sample(x)':x,'Differnce':differ,'- sign':A,'+ sign':B})
print(D)   #    gives data frame
print('Calulated value of Z=%.3f'%(calZ))
tabZ= 1.96
print('Tabulated value of Z=%.3f'%(tabZ))
if calZ<tabZ:
    print('Accept Ho at 5% level of significance')
    print ('RESULT:-120 is population median of give sample x')
else:
    print('reject Ho at 5% level of significance')
    print ('RESULT:-120 is not population median of give sample x')



# sign test for large paired sample

x=np.array([108,104,103,112,99,105,102,112,119,106,125,96,107,115,101,110,
            103,105,124,113,111,100,122,124,104,97,112,109,119,101])
y=np.array([103,116,106,104,99,94,110,128,106,103,120,98,117,130,100,101,96,
           99,120,116,100,101,108,118,95,100,105,103,99,95])
d=x-y      # difference array
T1=sum(d>0)     #No of positive sign
A=(d>0)
T2=sum(d<0)     # No of negative sign
B=(d<0)
T=min(T1,T2)    # No of fever sign
N=len(x)
mu=N/2
sigma=np.sqrt(N/4)
calZ=np.abs((T-mu)/sigma)
D=pd.DataFrame({'Sample1(x)':x,'Sample2(y)':y,'Differnce':d,'- sign':A,'+ sign':B})
print(D)   #    gives data frame
print('Calulated value of Z=%.3f'%(calZ))
tabZ= 1.96
print('Tabulated value of Z=%.3f'%(tabZ))
if calZ<tabZ:
    print('Accept Ho at 5% level of significance')
    print ('RESULT:-Population median of both sample are same')
else:
    print('reject Ho at 5% level of significance')
    print ('RESULT:-Population median of both sample are different.')




