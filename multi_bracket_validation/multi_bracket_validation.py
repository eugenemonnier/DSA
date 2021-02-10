def multi_bracket_validation(input):
  left_bracket_dict = { 
    '{' : '}',
    '(' : ')',
    '[' : ']'
    }
  right_bracket_dict = { 
    '}' : 0,
    ')' : 0,
    ']' : 0
    }
  prev_bracket = list()
  for char in input:
    if char in left_bracket_dict:
      right_bracket_dict[left_bracket_dict[char]] += 1
      prev_bracket.insert(0,left_bracket_dict[char])
    elif char in right_bracket_dict:
      if prev_bracket[0] != char:
        return False
      else:
        right_bracket_dict[char] -= 1
        prev_bracket.pop(0)

  if (right_bracket_dict['}'] == 0 and
      right_bracket_dict[')'] == 0 and
      right_bracket_dict[']'] == 0): return True
  else: return False

print(multi_bracket_validation('{}(){}'))
print(multi_bracket_validation('{}'))
print(multi_bracket_validation('()[[Extra Characters]]'))
print(multi_bracket_validation("(){}[[]]"))
print(multi_bracket_validation('{}{Code}[Fellows](())'))
print(multi_bracket_validation('[({}]'))
print(multi_bracket_validation('(]('))
print(multi_bracket_validation('{(})'))