# https://university.ylab.site/python/lecture-3-hw/

"""
Задача №1.
Напишите функцию-декоратор, которая сохранит (закэширует) значение 
декорируемой функции multiplier (Чистая функция). Если декорируемая 
функци будет вызвана повторно с теми же параметрами - декоратор должен 
вернуть сохраненный результат, не выполняя функцию.
"""
cache_dict: dict[int: int] = {1: 2, 3: 6, 7: 14, 12: 24}

def cache(cache_dict: dict):
    print(" cache has been worked")
    def cache_decorator(func):
        #print('cache_decorator has been worked!')
        def wrapper():
            print('wrapper has been worked')
            #print(kwargs)
            """if args in cache_dict:
                print(f'{args} loaded from cache')
            else:
                cache_dict[args] = func(*args, **kwargs)"""
        return wrapper
    return cache_decorator

@cache
def multiplier(number: int) -> int:
    return number * 2

for i in range(10):
    multiplier(i)

print(cache_dict)


