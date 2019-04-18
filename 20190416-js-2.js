// * 문제
// reverse 함수에 정수인 숫자를 인자로 받습니다.
// 그 숫자를 뒤집어서 return해주세요.

// x: 숫자
// return: 뒤집어진 숫자를 반환!


// 예들 들어,
// x: 1234
// return: 4321

// x: -1234
// return: -4321

// x: 1230
// return: 321

function reverse(x) {
  let num = x;
  let result ="";
  let minus = false;
  let zero = false;
  if (num < 0){
    num = Math.abs(num);
    minus = true;
  } 
  if (num === 0){
    return num;
  } else {
    let str = num.toString();
    let length = str.length
    for ( let i = length-1; i >= 0; i--){
      if ( str[i] !== "0" ){
        zero = true;
      }
      if ( zero ){
        result = result + str[i];
      }
    }
  
  
    if (minus === true){
      result = "-" + result;
    }
    console.log("결과 : " + result);
    
    result = parseInt (result);
    return result;
  }
}

reverse(8376);
