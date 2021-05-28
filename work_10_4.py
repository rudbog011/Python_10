print('Введите символ:')
s = input()
if 1040 <= ord(s) <= 1071:
    s = s.lower()
    print(s)
elif 1072 <= ord(s) <= 1103:
    s = s.upper()
    print(s.upper())
else:
    print(s)
