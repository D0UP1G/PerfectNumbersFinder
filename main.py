from sys import stdout


def update_num(x):  # замените на ваш цикл
    stdout.write('\r' + 'Текущее число: %d' % x)
    stdout.flush()

x = 0
print(x)

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

tnum = (6, 28, 496, 8128)

while len(tnum)<=10:

    x+=1

    if is_perfect(x):

          # Measure the start time

        end_time = timeit.default_timer()  # Measure the end time

        execution_time = end_time - start_time  # Calculate the execution time

        with open('file.txt', 'a', encoding='UTF-8') as file:
            file.write(str(x)+'-'+ str(execution_time) +'\n')
        
    else:
        logging.info(f'{x}')

    
        

    update_num(x)
