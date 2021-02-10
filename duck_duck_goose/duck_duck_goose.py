from collections import deque
def duck_duck_goose(arr,k):
  index = 0
  while len(arr) > 1:
    arr = deque(arr)
    arr.rotate(-3)
    arr.pop()
    print(arr)
  return arr[0]

print(duck_duck_goose([1,2,3,4,5],3))
