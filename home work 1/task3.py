# https://university.ylab.site/python/lecture-1-hw/

"""
Задача №3.
Написать метод zeros, который принимает на вход целое число (integer) и 
возвращает количество конечных нулей в факториале 
(N! = 1 * 2 * 3 * ... * N) заданного числа
"""
# нужно попробовать вычитать по одному до значения кратному пяти

def zeros(n: int) -> int:
    zeros_counter:int = 0
    
    degree: int = 0
    while 5 ** (degree + 1) < n:
        degree += 1
    print("n degree: " + str(degree))

    for i in range(degree):
        m: int = n
        j: int = 0
        while 5 ** (i) < m:
            print('m: ' + str(m))
            m = m - 5 ** (i + 1)
            zeros_counter += 1
        #j += 1


    """i:int = 0
    while n >= 5:

        n = n - 5
        zeros_counter += 1"""

    return zeros_counter 

print('0 --- ' + str(zeros(0)) + ' -> 0', end='\n\n') 
print('6 --- ' + str(zeros(6)) + ' -> 1', end='\n\n') 
print('30 --- ' + str(zeros(30)) + ' -> 7', end='\n\n') 
print('124 --- ' + str(zeros(124)) + ' -> 28', end='\n\n') 
print('126 --- ' + str(zeros(126)) + ' -> 31', end='\n\n') 

#assert zeros(0) == 0
#assert zeros(6) == 1
#assert zeros(30) == 7