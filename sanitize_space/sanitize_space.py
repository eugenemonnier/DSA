def sanitize(url):
  return url.replace(' ', '%20')

def sanitize_no_builtin(url):
  url_list = url.split()
  sanitized = ''
  for char in range(len(url_list) - 1):
    sanitized += url_list[char] + '%20'
  sanitized += url_list[len(url_list) - 1]
  return sanitized

def sanitize_list_comp(url):
  url_list = [i for j in url.split() for i in (j, ' ')][:-1]
  for elem in range(len(url_list)):
    if url_list[elem] == ' ': url_list[elem] = '%20'
  return ''.join(url_list)

print(sanitize("http://code.org/hour of code.html"))
print(sanitize_no_builtin("http://code.org/hour of code.html"))
print(sanitize_list_comp("http://code.org/hour of code.html"))
