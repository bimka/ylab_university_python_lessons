"""
Задача №2.
Надо написать декоратор для повторного выполнения декорируемой 
функции через некоторое время. Использует наивный экспоненциальный 
рост времени повтора (factor) до граничного времени ожидания 
(border_sleep_time)
"""
import time

def call(
         call_count, 
         start_sleep_time, 
         factor, 
         border_sleep_time
         ):

    def call_decorator(func):          

        def wrapper(*args, **kwargs):
            t = 1
            ola = 0

            print(f'Количество запусков = {call_count}')
            print('Начало работсы')            

            for i in range(call_count):
                time.sleep(t)
                if t < border_sleep_time:
                    t = start_sleep_time * 2**(ola)
                else:
                    t = border_sleep_time
                print(f'Запуск номер {i + 1}. Ожидание: {t} секунд. Результат декорируемой фенкции = {func(*args, **kwargs)}')
                if ola < factor:
                    ola += 1
                else:
                    break

            print('Конец работы')

        return wrapper        
    return call_decorator




@call(
      call_count=3, 
      start_sleep_time=3, 
      factor=3, 
      border_sleep_time=10)
def my_func():
    return 'Hello, world!'

my_func()