#https://university.ylab.site/python/lecture-2-hw/

"""
Задача №1.
Написать класс CyclicIterator. Итератор должен итерироваться по 
итерируемому объекту (list, tuple, set, range, Range2 и т.д.), 
и когда достгнет последнего элемента начинать сначала.
"""

class CyclicIterator:
    def __init__(self, stop_value: int):
        self.current = -1
        self.stop_value = len(stop_value) - 1


    def __iter__(self):
        return self


    def __next__(self):
        if self.current < self.stop_value:
            self.current += 1
        else:
            self.current = 0
        return self.current 


cyclic_iterator = CyclicIterator(range(3))
for i in cyclic_iterator:
    print(i)