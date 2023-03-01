#Текст зашифрован на русском языке.
# В тексте используются все буквы русского алфавита, кроме буквы Ё.


in_data = str(input())
j = int(input())
word = ""

letters = "абвгдежзийклмнопрстуфхцчшщъыьэюя"

for i in range(j):
  k = i
  letter = {}
  
  while k <= len(in_data) - 1:
    if in_data[k] in letter:
      letter[in_data[k]] += 1
    else:
      letter[in_data[k]] = 1
    k = k + j
  
  k = 0
  for m in letter:
    if letter[m] > k:
      k = letter[m]
      let = letters.find(m)
  k = i
  in_data = list(in_data)
 
  while k <= len(in_data) - 1:
    in_data[k] = letters[letters.find(in_data[k]) - 1]
    k = k + j

for i in in_data:
  word += i

print(word)
