import logging 
import sys 
sys.set_int_max_str_digits(2147483647)

x = 26926

logging.basicConfig(filename='logs.log', level=logging.INFO)

class Number():
    def __init__(self, i:int, is_perfect:bool = False):
        self.checked = 2**i-1
        self.is_perfect = is_perfect
import random
def fermat_test(n, k=100):
	if n <= 1:
		return False
	if n % 2 == 0:
		return False
	for _ in range(k):
		a = random.randint(1, n-1)
		if pow(a, n-1, n) != 1:
			return False
		return True  

def find_perfect_number(i:int):
    Xnum = Number(i)
    if Xnum.is_perfect != True:
        if fermat_test(Xnum.checked):
            Xnum.is_perfect = True
            
    return Xnum.is_perfect

while True:
    print(x)
    x+= 1
    if find_perfect_number(x):
        logging.info(f"p:{x}")
