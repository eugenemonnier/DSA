def sanitize(url):
  return url.replace(' ', '%20')

def sanitize_no_builtin(url):
  url_list = url.split()
  sanitized = ''
  for char in range(len(url_list) - 1):
    sanitized += url_list[char] + '%20'
  sanitized += url_list[len(url_list) - 1]
  return sanitized

print(sanitize("http://code.org/hour of code.html"))
print(sanitize_no_builtin("http://code.org/hour of code.html"))