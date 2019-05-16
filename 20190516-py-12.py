# * 코드카타
# recursion이 들어가도록 reverse 메서드 사용은 당연히 금지입니다!
# str 이라는 'string'을 넘겨주면 글자순서를 바꿔서 return해주세요.
# 
# input: 'hello'
# output: 'olleh'




def reverseString(str):
  result = str[0]
  str = str[1:]
  
  if len(str) == 0:
    return result
  else:
    return reverseString(str) + result
