# *문제
# 
# 다음과 같이 input이 주어졌을 때,
# 같은 알파벳으로 이루어진 단어끼리 묶어주세요.
# 
# 
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# 
# output에서 순서는 상관없습니다.



def groupAnagrams(strs):
  result = []

  while strs != [] :
    array = []
    num1 = len(strs)-1
    while num1 > 0:
      match = len(strs[0])
      num2 = 0
      while num2 < len(strs[0]) :
        if strs[num1].find(strs[0][num2]) != -1 :
          match -= 1
        if match == 0 :
          array.append(strs[num1])
          strs.remove(strs[num1])
          
        num2 += 1
        
      num1 -= 1
      
    array.insert(0, strs[0])
    strs.remove(strs[0])
    result.append(array)
  return result
  
print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
