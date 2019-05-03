#문제
#양수로 이루어진 m x n 그리드를 인자로 드립니다.
#상단 왼쪽에서 시작하여, 하단 오른쪽까지 가는 길의 요소를 다 더했을 때,가장 작은 합을 찾아서 return 해주세요.
#
#한 지점에서 우측이나 아래로만 이동할 수 있습니다.
#
#Input:
#[
#  [1,3,1],
#  [1,5,1],
#  [4,2,1]
#]
#
#Output: 7
#
#설명: 1→3→1→1→1 의 합이 제일 작음
#
#
#


def minPathSum(data):
  xLength = len(data[0])
  yLength = len(data)
  distance = xLength + yLength - 2
  
  num = 0
  while num < xLength :
    if num > 0 :
      data[0][num] = data[0][num] + data[0][num-1]
    num += 1

  num = 0
  while num < yLength :
    if num > 0 :
      data[num][0] = data[num][0] + data[num-1][0]
    num += 1


  yNum = 1
  while yNum < yLength :
    xNum = 1 
    while xNum < xLength :
      if data[yNum][xNum-1] >= data[yNum-1][xNum] :
        data[yNum][xNum] = data[yNum][xNum] + data[yNum-1][xNum]
        print("바뀌었다!", data[yNum][xNum])
      else :
        data[yNum][xNum] = data[yNum][xNum] + data[yNum][xNum-1]
        print("바뀌었다!", data[yNum][xNum])
      xNum += 1
    yNum += 1
  print(data)
  
  return data[yLength-1][xLength-1]
