# * code kata
# nums라는 정렬되지 않은 숫자 배열을 주면, 오름차순(1,2,3..10) 으로 정렬된 배열을 return해주세요.
# 선택정렬 알고리즘으로 구현하셔야겠죠??



def selectionSort(nums):
  num1 = 0
  while num1 < len(nums) - 1:
    num2 = num1+1
    while num2 < len(nums) :
      if nums[num1] > nums[num2]:
        nums[num1], nums[num2] = nums[num2], nums[num1]
      num2 += 1
    num1 += 1
  
  return nums
  
print(selectionSort([3,6,8,2,4,12,43]))
