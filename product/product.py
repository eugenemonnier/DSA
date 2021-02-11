def product(arr):
  arr.sort()
  low = arr[0] * arr[1] * arr[len(arr) - 1]
  high = arr[len(arr) - 1] * arr[len(arr) - 2] * arr[len(arr) - 3]
  if (low > high): return low
  else: return high

print(product([-10, 10, 4, -3, 1, 0]))
print(product([18, 3, 42, 17, 9, 27]))
print(product([4, 0, -5, 3, -1, -6, 2]))