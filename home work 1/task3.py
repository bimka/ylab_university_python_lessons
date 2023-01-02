"""
Задача №3.
Написать метод zeros, который принимает на вход целое число (integer) и 
возвращает количество конечных нулей в факториале 
(N! = 1 * 2 * 3 * ... * N) заданного числа
"""
# нужно попробовать вычитать по одному до значения кратному пяти

def zeros(n: int) -> int:
    zeros_counter:int = 0
    
    while n % 5 != 0:
        n = n - 1
    
    degree: int = 0
    while 5 ** (degree ) < n:
        degree += 1

    for i in range(degree):
        m: int = n
        while 5 ** (i+1) <= m:
            m = m - 5 ** (i + 1)
            zeros_counter += 1

    return zeros_counter 

assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7