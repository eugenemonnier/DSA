def insert_array_shift(arr, val):
  arr.insert(len(arr)//2, val)
  return arr

print(insert_array_shift([2,4,6,8], 5))