"""
Задача №4.
Написать метод bananas, который принимает на вход строку и возвращает  
количество слов 'banana' в строке.
"""
import copy

def bananas(s: str) -> set:
    result = set()
    word = 'banana'

    if len(s) < len(word):
        return result

    def recursion(buffer: str, s_index: int, word_index: int, i) -> set:
        #print(f'{i}-> s_index: {s_index}   word_index: {word_index}')
        #if len(s) < word_index:
        if buffer.replace('-', '') == word:
            #print(f'len_s: {len(s)}, word_index: {word_index}')
            result.add(buffer + '-' * (len(s) - len(buffer)))
        i += 1
        if len(s) > s_index :
            for j in range(s_index, len(s)):
                print(f's_index: {s_index}, word_index: {word_index}')
                if word_index < len(word) and s[s_index] == word[word_index]: 
                    buffer += s[s_index]
                    s_index += 1
                    word_index += 1
                else:
                    s_index += 1
                recursion('-' * (s_index - len(buffer)) + buffer, 
                        s_index, 
                        word_index, 
                        i)

        return result
    st = set()
    def f(ss, m, n):
        if n > 5:
            st.add(ss + '-'*(len(s)-m))
        elif m < len(s):
            for i in range(m, len(s)):
                if s[i] == 'banana'[n]:
                    f(ss+'-'*(i-m)+s[i], i+1, n+1)
        return
    f('', 0, 0)
    return st  


    #return recursion(buffer='', s_index=0, word_index=0, i = 0)

#print("banann: -> " + str(bananas("banann")), end='\n\n')
#print("banana: -> " + str(bananas("banana")), end='\n\n')
print("bbananana: -> " + str(bananas("bbananana")), end='\n\n')

'''assert bananas("banann") == set()
assert bananas("banana") == {"banana"}
assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", \
                                "b-a--nana", "-banan--a", "b-ana--na", \
                                "b---anana", "-bana--na", "-ba--nana", \
                                "b-anan--a", "-ban--ana", "b-anana--"}
assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", \
                               "b--anana", "banana--", "banan--a"}'''
