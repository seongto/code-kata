# *문제 
# 숫자로 이루어진 리스트 nums를 인자로 주면,
# 그 안에서 어떤 연속적인 요소를 더했을 때 가장 큰 값이 나오나요?
# 가장 큰 값을 찾아 return해주세요.
# 
# 
# Input: [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# 설명: [4,-1,2,1] 를 더하면 6이 가장 크기 때문


def maxSubArray(nums):
  result = 0
  num1 = 0
  while num1 < len(nums):
    num2 = num1
    sum = 0
    while num2 < len(nums):
      sum = nums[num2] + sum
      if sum > result:
        result = sum
      num2 += 1
    num1 += 1
  return result

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))



# ------------------------- 아래는 천재적인 압축 코드

def maxSubArray(nums):
  for i in range(1, len(nums)):
    if nums[i-1] > 0:
      nums[i] += nums[i-1]
      
  print(nums)
  return max(nums)
  
maxSubArray([-2,1, 3, 4, -3, 3])
