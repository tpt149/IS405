import random

listNo = []

for x in range(20):
    listNo.append(random.uniform(1,100))
print(listNo)

rddNumber1 = sc.parallelize(listNo)
mean1 = rddNumber1.reduce(lambda a, b: a + b) / rddNumber1.count()
print(mean1)

rddNumber2 =sc.parallelize(listNo)
product = rddNumber2.reduce(lambda a, b: a * b) 
mean2 = pow(product, 1/rddNumber2.count())
print(mean2)

broadMean = sc.broadcast(mean2)
rdd = rddNumber1.map(lambda x: (x - broadMean.value) **2)
variance = rdd.reduce(lambda a, b: a + b) / rdd.count()
print(variance)

import math
stdDev = math.sqrt(variance)
print(stdDev)

file = open('phanso.txt', 'r')
lines = file.readlines()
file.close()

for i in range(len(lines)):
  lines[i] = lines[i].strip('\n').split('/')

data = sc.parallelize(lines)
numerators = data.map(lambda x: int(x[0]))
denominators = data.map(lambda x: int(x[1]))

from math import gcd

common_denominator = denominators.reduce(lambda a,b: a*b//gcd(a,b)) 
fractions = numerators.zip(denominators)
frac1 = fractions.map(lambda x: (x[0]*common_denominator/x[1], common_denominator))
sum_numerators = frac1.map(lambda x: x[0]).reduce(lambda a,b: a+b)
total = [sum_numerators, common_denominator]
print(f"Kết quả : {int(total[0])}/{total[1]}")


