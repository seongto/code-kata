// * 문제
// 숫자인 x를 인자로 넘겨주면, 뒤집은 모양이 x와 똑같은지 여부를 반환해주세요.
// x: 숫자
// return: true or false (뒤집은 모양이 x와 똑같은지 여부)

// 예를 들어,
// num = 123
// return false 
// => 뒤집은 모양이 321 이기 때문

// num = 1221
// return true 
// => 뒤집은 모양이 1221 이기 때문

// num = -121
// return false 
// => 뒤집은 모양이 121- 이기 때문

// num = 10
// return false 
// => 뒤집은 모양이 01 이기 때문




function sameReverse(num) {
  let str = num.toString();
  console.log(str);
  let result = "";
  for ( let i = 0; i < str.length; i++){
    result = str[i] + result;
  }
  console.log(result);
  if (result === str){
    return true
  } else {
    return false
  }
}

sameReverse(12345);
