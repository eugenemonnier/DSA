def anagrams(s1, s2):
  s1 = s1.replace(' ', '').lower()
  s2 = s2.replace(' ', '').lower()
  s1_dict, s2_dict = {}, {}
  if len(s1) != len(s2): return False
  for i in range(len(s1)):
    if not s1[i] in s1_dict: s1_dict[s1[i]] = 1
    else: s1_dict[s1[i]] += 1
    if not s2[i] in s2_dict: s2_dict[s2[i]] = 1
    else: s2_dict[s2[i]] += 1
  if s1_dict == s2_dict: return True
  else: return False

print(anagrams("Eleven plus two", "Twelve plus one"))
print(anagrams("Clint Eastwood", "Old West Action"))
print(anagrams("Software", "Swear often"))
print(anagrams("Astronomers", "Moon starers"))