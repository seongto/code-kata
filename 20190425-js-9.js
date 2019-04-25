// * 문제
// nums는 숫자로 이루어진 배열입니다. 
// 가장 자주 등장한 숫자를 k 개수만큼 return해주세요.

// nums = [1,1,1,2,2,3],
// k = 2
// return [1,2]

// nums = [1]
// k = 1
// return [1]
//
//

function topK(nums, k) {
  let result = [];
  let dic = {};
  for (let i = 0; i < nums.length; i++){
    num = 0;
    for (let j = 0; j < nums.length; j++){
      if (nums[i] === nums[j]){
        num = num +1;
      }
    }
    dic[num] = nums[i]
  }
  let array = Object.keys(dic);
  array.sort(function(a, b){return b - a});
  
  for ( let i =0; i < k; i++){
    result.push(dic[array[i]])
  }
  result.sort();
  
  return result
}
