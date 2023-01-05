"""
Задача №5.
Написать метод count_find_num, который принимает на вход список 
простых множителей (primesL) и целое число, предел (limit), после 
чего попробуйте сгенерировать по порядку все числа. Меньшие значения 
предела, которые имеют вссе и тольк простые множители простыж чисел primeesL.
"""
import math
import copy

def count_find_num(primesL: list, limit: int) -> list:
    multiplication_result: int = 0
    max_multiplication_value: int = math.prod(primesL)
    list_of_prime_factors: list = [primesL]

    for i in primesL:
        ola = copy.copy(primesL)
        #print(f'Исходник {ola}')
        while (math.prod(ola) *  i ) <= limit:            
            ola.append(i)
            if math.prod(ola) > max_multiplication_value:
                max_multiplication_value = math.prod(ola)
            #print(f'Перемножение всех элементов: {math.prod(ola)}')
            #print(ola)
            list_of_prime_factors.append(copy.copy(ola))
            #print(list_of_prime_factors)
        #print()
    print(list_of_prime_factors)

    
    
    set_prime_factors = set(list_of_prime_factors)


    counter_multiple_value = len(set_prime_factors)
    return [counter_multiple_value, max_multiplication_value]


# primesL = [2, 5, 7]
# limit = 500
# print(count_find_num(primesL, limit))
# # [5, 490]

primesL = [2, 3]
limit = 200
print(count_find_num(primesL, limit))# [13, 192]

# primesL = [2, 3]
# limit = 200
# assert count_find_num(primesL, limit) == [13, 192]

# primesL = [2, 5]
# limit = 200
# assert count_find_num(primesL, limit) == [8, 200]

# primesL = [2, 3, 5]
# limit = 500
# assert count_find_num(primesL, limit) == [12, 480]

# primesL = [2, 3, 5]
# limit = 1000
# assert count_find_num(primesL, limit) == [19, 960]

# primesL = [2, 3, 47]
# limit = 200
# assert count_find_num(primesL, limit) == []