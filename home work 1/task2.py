"""
Задача №2.
Написать метод int32_to_ip, который принимает на вход 32-битное целое 
число (int) и возвращает строковое представление его в виде IPv4-адреса.
"""

def int32_to_ip(int32: int) -> str:
    if int32 > 4294967295:
        return "The value is too high!! Try to choose a smaller value."

    def convert_to_binary(decimal_value: int) -> str:
        if decimal_value == 0:
            return '0'
    
        division_result: int = decimal_value
        reverse_binary_value: str = ''
    
        while division_result != 0:
            reverse_binary_value += str(division_result % 2)
            division_result = division_result // 2

        binary_value: str = reverse_binary_value[::-1]
        return binary_value


    def split_into_octets(binary_value: str) -> str:
        reverse_binary_value: str = binary_value[::-1]

        i: int = 0
        reverse_list_of_octets: list = []
        while i < len(reverse_binary_value):
            octet:str = reverse_binary_value[i:i+8]
            if len(octet) < 8:
                octet = octet + (8 - len(octet)) * '0'
            reverse_list_of_octets.append(octet[::-1])
            i += 8

        while len(reverse_list_of_octets) < 4:
            reverse_list_of_octets.append('00000000')

        list_of_octets: list = reverse_list_of_octets[::-1]
        value_devided_into_octets: str = '.'.join(list_of_octets)
        return value_devided_into_octets

    def convert_octet_to_decimal(double_octets:str) -> str:
        list_of_double_octets: list = double_octets.split('.')
        list_of_decimal_octets: list = []

        for double_octet in list_of_double_octets:
            decimal_octet = 0
            reverce_double_octet: str = double_octet[::-1]

            i:int = 0
            while i < len(reverce_double_octet):
                decimal_octet += int(reverce_double_octet[i]) * 2 ** i
                i += 1
            
            list_of_decimal_octets.append(str(decimal_octet))

        value_of_decimal_octets: str = '.'.join(list_of_decimal_octets)
        return value_of_decimal_octets
    

    binary_value: str = convert_to_binary(int32)
    value_split_into_octets: str = split_into_octets(binary_value)
    decimal_value_split_into_octets: str = convert_octet_to_decimal(value_split_into_octets)
    return decimal_value_split_into_octets


assert int32_to_ip(2154959208) == "128.114.17.104"
assert int32_to_ip(0) == "0.0.0.0"
assert int32_to_ip(2149583361) == "128.32.10.1"