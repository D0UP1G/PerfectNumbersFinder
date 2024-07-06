import logging
import sys
sys.set_int_max_str_digits(10000)

x = 0


logging.basicConfig(filename="logs.log",level=logging.INFO)

def PerfectNumGenerator(x):
    y = 0
    for i in range(1,x+1):
        if x%i == 0:
            y+=i
    if y == x+1:
        res = 2**(x-1) * (2**x-1)
        logging.info(f"{x}: {res}")
        return res
        
    else:
        return False

while True:
    x+=1
    perfect = PerfectNumGenerator(x)
    if perfect:
        print(f'I FOUND NEW PERFECT NUMBER!: {perfect}')
