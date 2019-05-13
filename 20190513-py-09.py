# * 오늘의 코드 카타
# 오름차순인 숫자 nums 배열과 찾아야할 target을 인자로 주면,
# target이 몇 번째 index인지 return 해주세요.
# 
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# 
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# 설명: 찾지 못하면 -1로 return 해주세요.
# 
# * nums 배열에 있는 요소는 서로 중복된 값이 없습니다.
# * 이진탐색으로 찾기



def search(nums, target) :
  idx = 0
  check = True
  while check == True :
    if len(nums) <= 2:
      if nums[0] == target:
        return idx
      elif nums[1] == target:
        return idx+1
      else :
        return -1
    loc = len(nums)//2
    print("현재 nums[roc]은 ",nums[loc])

    if nums[loc] == target:
      check = False
      return loc
    elif target < nums[loc]:
      nums = nums[0:loc]
      print("타겟이 작음. 현재 nums : ",nums)
    else :
      nums = nums[loc+1:]
      print("타겟이 큼. 현재 nums : ",nums)
      idx = idx + loc+1




# ---------------- 모델 솔루션 ----------------


def search(nums, target):
  l, r = 0, len(nums) - 1
  while l <= r:
    mid = (l + r) // 2
    if nums[mid] < target:
      l = mid + 1
    elif nums[mid] > target:
      r = mid - 1
    else:
      return mid
  return -1
