def binary_search(arr, key):
  curr_index, min_index, max_index = 0, 0, len(arr) - 1
  while True:
    curr_index = (min_index + max_index) // 2
    if key == arr[curr_index]: return curr_index
    elif max_index < min_index: return - 1
    elif key > arr[curr_index]: 
      min_index = curr_index + 1
    elif key < arr[curr_index]:
      max_index = curr_index - 1

print(binary_search([4,8,15,16,23,42], 15))
print(binary_search([11,22,33,44,55,66,77], 90))
print(binary_search([1, 2, 3, 5, 6, 7], 4))
print(binary_search([1,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59], 37))