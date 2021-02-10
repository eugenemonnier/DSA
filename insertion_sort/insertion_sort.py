def insertion_sort(arr):
  for index, num in enumerate(arr):
    i = index
    while i > 0 and num < arr[i - 1]:
      arr[i] = arr[i - 1]
      i -= 1
    arr[i] = num
  return arr

print(insertion_sort([8,4,23,42,16,15]))
print(insertion_sort([20,18,12,8,5,-2]))
print(insertion_sort([5,12,7,5,5,7]))
print(insertion_sort([2,3,5,7,13,11]))