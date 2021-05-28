print('Введите две строчные латинские буквы:')
a = input()
b = input()
if ord(b) < ord(a):
    k = b
    b = a
    a = k
for i in range(ord(a), ord(b)+1):
    print(chr(i))