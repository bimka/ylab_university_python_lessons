# https://university.ylab.site/python/lecture-1-hw/#zadacha-no2.
# https://service-calc.ru/raznoe/sistemy-schisleniya-perevod#i-7
# https://calculatori.ru/perevod-chisel.html

"""
Задача №2.
Написать метод int32_to_ip, который принимает на вход 32-битное целое 
число (int) и возвращает строковое представление его в виде IPv4-адреса.
"""

def int32_to_ip(int32: int) -> str:
  binary_value: int = 0
  
  def convert_to_binary(decimal_value: int) -> int:
    division_value: int = decimal_value
    binary_value: str = ''
    
    while division_value != 0:
      binary_value += ''


#assert int32_to_ip(2154959208) == "128.114.17.104"
#assert int32_to_ip(0) == "0.0.0.0"
#assert int32_to_ip(2149583361) == "128.32.10.1"