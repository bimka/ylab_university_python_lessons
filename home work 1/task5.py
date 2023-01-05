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
    list_of_prime_factors: list = [primesL]

    def find_max_multiplication_value(divisors_list: list, limit: int) -> int:
        max_multiplication_value = math.prod(divisors_list)
        for i in divisors_list:
            while (max_multiplication_value * i) <= limit:
                divisors_list.append(i)
                if math.prod(divisors_list) > max_multiplication_value:
                    max_multiplication_value = math.prod(divisors_list)
        return max_multiplication_value


    def find_multipliers_in_a_row(lst: list, max_value: int) -> list:
        list_of_recurring_multipliers = []
        for i in lst:
            ola = copy.copy(lst)
            while (math.prod(ola) *  i ) <= max_value:            
                ola.append(i)
                list_of_recurring_multipliers.append(copy.copy(ola))
        return list_of_recurring_multipliers
        
    
    max_value = find_max_multiplication_value(copy.copy(primesL), limit)


    def add_a_divisors_to_the_end(lst: list) -> list:
        for j in lst:
            list_of_additional_divisors = []
            len_lst = len(j)
            i = 0
            while i < len_lst:
                ola = [j[i]]
                ola.extend(j)
                list_of_additional_divisors.append(ola)
                i += 1
        
        return list_of_additional_divisors


    i = 10
    while i > 0:
        additional_ending = add_a_divisors_to_the_end(list_of_prime_factors)
        list_of_prime_factors.extend(additional_ending)
        i -= 1

    recurring_multipliersfind = find_multipliers_in_a_row(primesL, max_value)
    list_of_prime_factors.extend(recurring_multipliersfind )


    ola = []
    for j in list_of_prime_factors:
        if math.prod(j) <=  max_value:
            ola.append(sorted(j))

    lala = []
    for i in ola:
        if i not in lala:
            lala.append(i)

    print(lala)

    print(len(lala))    
    
    return max_value


# primesL = [2, 5, 7]
# limit = 500
# print(count_find_num(primesL, limit))
# # [5, 490]

# primesL = [2, 3]
# limit = 200
# print(count_find_num(primesL, limit))# [13, 192]

# primesL = [2, 3]
# limit = 200
# assert count_find_num(primesL, limit) == [13, 192]

primesL = [2, 5]
limit = 200
print(count_find_num(primesL, limit))# [8, 200]
# assert count_find_num(primesL, limit) == [8, 200]

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
