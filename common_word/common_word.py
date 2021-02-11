import string
def most_common_word(s):
  max_word_count = 0
  output = ''
  word_dict = {}
  word_list = s.lower().translate(str.maketrans('', '', string.punctuation)).split()
  for word in word_list:
    if not word in word_dict: word_dict[word] = 1
    else: word_dict[word] += 1
    if word_dict[word] > max_word_count:
      output = word
      max_word_count = word_dict[word]
  return output

print(most_common_word("In a galaxy far far away"))
print(most_common_word('Taco cat ate a taco'))
print(most_common_word('No. Try not. Do or do not. There is no try.'))
print(most_common_word('Test. This is only a test. If this were not a test, I would not have said it was a test.'))