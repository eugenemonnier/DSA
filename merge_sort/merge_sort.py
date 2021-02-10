def merge_sort(arr):
  n = len(arr)

  if n > 1:
    mid = n // 2
    left = arr[0:mid]
    right = arr[mid:n + 1]

    left = merge_sort(left)
    right = merge_sort(right)
    merge(left, right, arr)
  
  return arr

def merge(left, right, arr):
  i, j, k = 0, 0, 0

  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      arr[k] = left[i]
      i += 1
    else:
      arr[k] = right[j]
      j += 1
    k += 1
  if i == len(left): arr[k:len(arr)] = right[j:len(right)]
  else: arr[k:len(arr)] = left[i:len(left)]
  return arr

print(merge_sort([100,20,30, 5]))
print(merge_sort([8,4,23,42,16,15]))