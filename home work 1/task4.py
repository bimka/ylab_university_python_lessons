"""
Задача №4.
Написать метод bananas, который принимает на вход строку и возвращает  
количество слов 'banana' в строке.
"""

def bananas(s: str) -> set:
    result = set()
    word = 'banana'

    if len(s) < len(word):
        return result

    def recursion(buffer, s_index, word_index) -> set:
        if word_index > 5:
            result.add(buffer + '-' * (len(s) - s_index))
        elif s_index < len(s):
            for i in range(s_index, len(s)):
                if s[i] == word[word_index]:
                    recursion(buffer+'-'*(i-s_index)+s[i], i+1, word_index+1)
        return result    
    
    return recursion(buffer='', s_index=0, word_index=0)

assert bananas("banann") == set()
assert bananas("banana") == {"banana"}
assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", \
                                "b-a--nana", "-banan--a", "b-ana--na",\
                                "b---anana", "-bana--na", "-ba--nana",\
                                "b-anan--a", "-ban--ana", "b-anana--"}
assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na",\
                                "b--anana", "banana--", "banan--a"}
