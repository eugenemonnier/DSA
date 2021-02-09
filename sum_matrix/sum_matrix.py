def sum_matrix(arr):
  matrix_sum = []
  for x in range(len(arr)):
    row_sum = 0
    for y in range(len(arr[x])):
      row_sum = row_sum + arr[x][y]
    matrix_sum.append(row_sum)
  return matrix_sum

print(sum_matrix([ [1, 2, 3], [3, 5, 7], [1, 7, 10] ]))
print(sum_matrix([ [1, 5, 3, 5], [-4, 7, 2], [-3, 12, 11], [2] ]))