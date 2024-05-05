import math
from collections import Counter
N=int(input("enter the number of elements:"))
numbers=[]
for i in range(N):
    num=float(input(f"enter number{i+1}:"))
    numbers.append(num)
mean=sum(numbers)/N
variance=0
for x in numbers:
    n1=(x-mean)**2
    variance=variance+n1
variance=variance/N
std_deviation=math.sqrt(variance)
counter=Counter(numbers)
max_freq=max(counter.values())
mode_values=[key for key,value in counter.items() if value==max_freq]
print("\nstatistics")
print("Mean:",mean)
print("Variance",variance)
print("standard deviation",std_deviation)
print("Mode:",mode_values[0])
