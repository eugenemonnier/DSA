import string, re
def repeated_words(s):
  word_dict = {}
  word_list = re.split('\s+', s.translate(str.maketrans('', '', string.punctuation)))
  for word in word_list:
    if not word.lower() in word_dict: word_dict[word.lower()] = 1
    else: return word.lower()
  return "No matching words"


print(repeated_words("No repeated words here. Just us mice."))
print(repeated_words("Once upon a time, there was a brave princess who..."))
print(repeated_words("It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."))
print(repeated_words("It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."))
