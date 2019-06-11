import os
import sys
import math
import random
import pycodestyle
sys.path.append('/home/sweidman/working/dice')
from dice import die

BASE_DIR = os.path.dirname('/home/sweidman/working')
random.choice([1, 2, 3, 4, 5, 6])
d = die.roll()
print(d)
tic = 0.1
num = 0.0
for i in range(40):
    num = num + tic
    print(math.ceil(num**2) * "*")

