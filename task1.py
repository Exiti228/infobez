#Реализовать программу симметричного шифрования вводимой строки,
#используя гаммирование по алгоритму Вернона (ключ — случайная двоичная последовательность).

import random
s = str(input())
letters = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
key = random.randint(0, 63)
word = ""

for i in s:
  let = bin(letters.index(i)^key)[2:]
  while len(let) < 6:
    let = "0" + let
  word += let

print("Ключ - ", key)
print(word)
