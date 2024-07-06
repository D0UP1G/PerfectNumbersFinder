import timeit
import logging
logging.basicConfig(filename='example.log', level=logging.INFO)
start_time = timeit.default_timer()

def is_perfect(number):
    if number%2 != 0:
        return False
    sum_divisors = 0
    for i in range(1, number):

        if number % i == 0:

            sum_divisors += i
    return sum_divisors == number


def sum_of_odd_squares(n): 
    result = 0 
    for i in range(1, 2*n+1, 2): 
        result += i**3
        update_num(result)
    return result

from sys import stdout
def update_num(x): 
    stdout.write('\r' + 'Текущее число: %d' % x)
    stdout.flush()

x = 2*2147483648

while True:
    x=x*2
    soos = sum_of_odd_squares(x)
    end_time = timeit.default_timer()
    execution_time = end_time - start_time
    if is_perfect(soos):
        
        with open('file.txt', 'a', encoding='UTF-8') as file:
            file.write(str(x)+':'+str(soos)+'-'+ str(execution_time) +'\n')
    logging.info(f'{x}:{soos} - {execution_time}')
    update_num(soos)



