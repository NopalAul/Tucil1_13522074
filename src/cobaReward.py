# long_string = "This is a long string and we want to find a substring within it."
# substring = "substring"

# index = long_string.find(substring)
# if index != -1:
#     print("Substring found at index:", index)
# else:
#     print("Substring not found")


long_string = [ '7A 55 E9 E9 1C 55',
                '55 7A 1C 7A E9 55',
                '55 1C 1C 55 E9 BD',
                'BD 1C 7A 1C 55 BD',
                'BD 55 BD 7A 1C 1C',
                '1C 55 55 7A 55 7A']
substring = '55'

for i in range(len(long_string)):
    print(f'longstring {i} : {long_string[i]}')
    index = long_string[i].find(substring)
    print(f'index : {index}')
    if index != -1:
        break
if index != -1:
    print("Substring found at index:", index)
else:
    print("Substring not found")