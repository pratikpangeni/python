#quadratic equation formula
import math
a=float(input('enter a:'))
b=float(input('enter b:'))
c=float(input('enter c:'))
d=(b*b)-(4*a*c)
print ('value d:',d)
alpha=(-b)-math.sqrt(d)/(2*a)
beta=(-b)+math.sqrt(d)/(2*a)
print ('the value is: ',alpha,'and',beta)
