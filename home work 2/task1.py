#https://university.ylab.site/python/lecture-2-hw/

"""
Задача №1.
Написать класс CyclicIterator. Итератор должен итерироваться по 
итерируемому объекту (list, tuple, set, range, Range2 и т.д.), 
и когда достгнет последнего элемента начинать сначала.
"""

class CyclicIterator:
    def __init__(self, value):
        self.value = value


    def __iter__(self):
        return self.value


    def __next__(self):
        return self.value



cyclic_iterator = CyclicIterator(range(3))
for i in cyclic_iterator:
    print(i)