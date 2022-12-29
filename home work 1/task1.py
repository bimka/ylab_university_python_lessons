"""
Задача №1.
Написать метод domain_name, который вернет домен из url адреса.
"""



import re

def domain_name(url: str) -> str:
  domain_name: str = ''
  
  url_without_protocol: str = re.split("://|www.", url)[-1]
  
  i: int = 0
  while url_without_protocol[i] != ".":
    domain_name += url_without_protocol[i]
    i += 1
  
  return domain_name
  
  
  
assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"