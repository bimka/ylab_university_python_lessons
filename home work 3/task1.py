# https://university.ylab.site/python/lecture-3-hw/

"""
Задача №1.
Напишите функцию-декоратор, которая сохранит (закэширует) значение 
декорируемой функции multiplier (Чистая функция). Если декорируемая 
функци будет вызвана повторно с теми же параметрами - декоратор должен 
вернуть сохраненный результат, не выполняя функцию.
"""
cache_dict: dict[int: int] = {1: 2, 3: 6, 7: 14, 12: 24}

def cache_decorator(func):
    def wrapper(*args, **kwargs):
        if args[0] in cache_dict:
            print(f'{args[0]} loaded from cache')
        else:
            cache_dict[args[0]] = func(*args, **kwargs)
    return wrapper

@cache_decorator
def multiplier(number: int) -> int:
    return number * 2

for i in range(10):
    multiplier(i)


