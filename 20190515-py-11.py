# nums라는 배열을 주면, 버블정렬 알고리즘으로 배열을 정렬해주세요.

def bubbleSort(arr):
  
  num1 = 0
  while num1 < len(arr)-1:
    num2 = 0
    while num2 < len(arr)-1-num1 :
      if arr[num2] > arr[num2+1]:
        arr[num2], arr[num2+1] = arr[num2+1], arr[num2]
      num2 += 1
    num1 += 1
  return arr
  
print(bubbleSort([5,6,3,2,8]))
