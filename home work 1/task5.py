"""
Задача №5.
Написать метод count_find_num, который принимает на вход список 
простых множителей (primesL) и целое число, предел (limit), после 
чего попробуйте сгенерировать по порядку все числа. Меньшие значения 
предела, которые имеют вссе и тольк простые множители простыж чисел primeesL.
"""
import math

def count_find_num(primesL: list, limit: int) -> list:
    list_of_prime_factors: list = [primesL]

    def add_a_divisors_to_the_end(lst: list) -> list:
        list_of_additional_divisors = []
        for j in lst:
            len_lst = len(j)
            i = 0
            while i < len_lst:
                ola = [j[i]]
                ola.extend(j)
                list_of_additional_divisors.append(ola)
                i += 1
        
        return list_of_additional_divisors
        

    def find_max_multiplication(divisors_list: list) -> int:
        max_multiplication_value = math.prod(primesL)
        for i in divisors_list:
            if math.prod(i) > max_multiplication_value:
                max_multiplication_value = math.prod(i)
        return max_multiplication_value


    i = len(primesL) + 3
    while i > 0:
        additional_ending = add_a_divisors_to_the_end(list_of_prime_factors)
        list_of_prime_factors.extend(additional_ending)
        i -= 1

    multipliers_less_limit = []
    for j in list_of_prime_factors:
        if math.prod(j) <=  limit:
            multipliers_less_limit.append(sorted(j))

    multipliers_without_repeats = []
    for i in multipliers_less_limit:
        if i not in multipliers_without_repeats:
            multipliers_without_repeats.append(i)

    max_value = find_max_multiplication(multipliers_without_repeats)
    len_of_multiplieк_list = len(multipliers_without_repeats)
    if len_of_multiplieк_list == 0:
        return []

    return [len_of_multiplieк_list, max_value]


primesL = [2, 3]
limit = 200
assert count_find_num(primesL, limit) == [13, 192]

primesL = [2, 5]
limit = 200
assert count_find_num(primesL, limit) == [8, 200]

primesL = [2, 5]
limit = 200
assert count_find_num(primesL, limit) == [8, 200]

primesL = [2, 3, 5]
limit = 500
assert count_find_num(primesL, limit) == [12, 480]

primesL = [2, 3, 5]
limit = 1000
assert count_find_num(primesL, limit) == [19, 960]

primesL = [2, 3, 47]
limit = 200
assert count_find_num(primesL, limit) == []
