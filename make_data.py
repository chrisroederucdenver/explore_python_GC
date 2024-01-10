#!/usr/bin/env python3

import csv
import random
from faker import Faker
from datetime import datetime


LOADS=100000

l=Faker('en_GB') 

f=open("test100.csv","w")
w=csv.writer(f)
w.writerow(('id', 'name', 'address', 'college', 'company', 'dob', 'age'))
for i in range(LOADS):
    w.writerow((i+1, l.name(), l.address(), \
        random.choice(['psg','sona','amirta','anna university']), \
        random.choice(['CTS','INFY','HTC']),(random.randrange(1950,1995,1), \
        random.randrange(1,13,1), \
        random.randrange(1,32,1)), \
        random.choice(range(0,100))))

f.close()


