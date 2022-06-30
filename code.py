# sd = squareRoot(sumOf([x-mean]^2) / (n-1))

# x = [10,20,30,40]

# mean = 25

# x1-mean --> 10-25 = -15  --> 225

# x2-mean --> 20-25 = -5  --> 25

# x3-mean --> 30-25 = 5  --> 25

# x4-mean --> 40-25 = 15 --> 225

# sum of --> 500

# 500/3 --> 166.7

# squareRoot --> 13


# ------------------------------------------------------------------------------

import pandas as pd
import math

x = [10,20,30,40]

n = len(x)

sum = 0

for i in x :
    sum = i+sum

mean = sum/n

print("Mean is " , mean)

squaredList=[]
for i in x :
    sub = i-mean
    sub = sub**2
    squaredList.append(sub)

sum = 0
for i in squaredList:
    sum = sum+i

divide = n-1

a = sum/divide

stdev = math.sqrt(a)

print("Standard Deviation using Algo is " , stdev)


