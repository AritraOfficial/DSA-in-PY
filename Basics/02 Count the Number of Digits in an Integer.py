n = 584300
num = n 
count = 0 
while num > 0:
    count += 1
    num //= 10
#print("Number of digits:", count)

# ---------- Count dights by help of logarithm ----------
from math import * 
def count_digits(n):
    if n == 0:
        return 1
    return int(log10(n)) + 1 