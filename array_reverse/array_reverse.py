def reverse_array(arr):
  rev_array = list()
  for i in range(len(arr)):
    rev_array.append(arr[len(arr) - i - 1])
  return rev_array

print(reverse_array([1,2,3,4,5]))