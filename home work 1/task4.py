"""
Задача №4.
Написать метод bananas, который принимает на вход строку и возвращает  
количество слов 'banana' в строке.
"""

def bananas(s: str) -> set:
    result = set()
    control_word: str = 'banana'
    buffer :str = ''
    len_s: int =  len(s)
    len_conrtol_word: int = len(control_word)

    print(s)

    if len_s < len_conrtol_word:
        return result

    def ola(s, control_word, buffer):
        i: int = 0 # счетчик для контрольного слова
        len_s = len(s)
        len_conrtol_word = len(control_word)

        for j in range(len_s):
            print(f'len_s: {len_s}, len_conrtol_word: {len_conrtol_word}')
            if len_s < len_conrtol_word:
                break
            if s[i] == control_word[0]:
                buffer += s[0]
                s = s[1:]
                control_word = control_word[1:]
                ola(s, control_word, buffer)
            else:
                buffer += '-'
                i += 1
            print(f"i: {i}, j: {j}, buffer: {buffer}")
            if i >= len_s:
                break
            print()
        return buffer

    buffer = ola(s, control_word, buffer)


    if buffer.replace('-', '') == control_word:
        result.add(buffer)


    return result


#print("banann: -> " + str(bananas("banann")), end='\n\n')
print("banana: -> " + str(bananas("banana")), end='\n\n')
#print("bbananana: -> " + str(bananas("bbananana")), end='\n\n')

'''assert bananas("banann") == set()
assert bananas("banana") == {"banana"}
assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", \
                                "b-a--nana", "-banan--a", "b-ana--na", \
                                "b---anana", "-bana--na", "-ba--nana", \
                                "b-anan--a", "-ban--ana", "b-anana--"}
assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", \
                               "b--anana", "banana--", "banan--a"}'''
