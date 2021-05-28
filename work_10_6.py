print('Введите строку:')
s = input()
num = ''
for i in range(len(s)):
    if 48 <= ord(s[i]) <= 57:
        num += s[i]
print(num)