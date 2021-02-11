def product(arr):
  if len(arr) < 3: return ValueError('Input does not contain enough elements.')
  if len(arr) == 3: 
    print('Well that was easy.')
    return arr[0] * arr[1] * arr[2]
  arr.sort()
  low = arr[0] * arr[1] * arr[len(arr) - 1]
  high = arr[len(arr) - 1] * arr[len(arr) - 2] * arr[len(arr) - 3]
  if (low > high): return low
  else: return high

print(product([-10, 10, 4, -3, 1, 0]))
print(product([18, 3, 42, 17, 9, 27]))
print(product([4, 0, -5, 3, -1, -6, 2]))
print(product([1000, 2000]))
print(product([100, 200, -1]))