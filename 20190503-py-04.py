#* 문제
#주어진 숫자 배열에서, 0을 배열의 마지막쪽으로 이동시켜주세요.
#원래 있던 숫자의 순서는 바꾸지 말아주세요.
#
#* 새로운 배열을 생성해서는 안 됩니다.
#
#Input: [0,1,0,3,12]
#Output: [1,3,12,0,0]
#


def moveZeroes(nums):
  length = len(nums)
  num = 0
  while num < length :
    if nums[num] == 0:
      nums.append(nums[num])
      nums.remove(nums[num])
    num +=1
  return nums
