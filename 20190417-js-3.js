// * 문제
// String 형인 str 인자에서 중복되지 않은 알파벳으로 이루어진 제일 긴 단어의 길이를 반환해주세요.

// str: 텍스트
// return: 중복되지 않은 알파벳 길이 (숫자 반환)


// 예를 들어,
// str = "abcabcabc"
// return은 3
// => 'abc' 가 제일 길기 때문

// str = "aaaaa"
// return은 1
// => 'a' 가 제일 길기 때문

// str = "sttrg"
// return은 3
// => 'trg' 가 제일 길기 때문


function getLengthOfStr(str) {
  let result = "";
  for (let i=0; i < str.length; i++){
    let match = "";
    let bool = true;
    for (let j = i; j < str.length; j++){
      
      for (let k = 0; k < match.length; k++){
        if (match[k] === str[j]){
          bool = false;
        }
      }
      if ( bool ){
        match = match + str[j];
        bool = true;
        // console.log(match);
        if (match.length > result.length){
          result = match;
          console.log(result);
        }
      }
    }
    
  }
  return result.length;
}

getLengthOfStr("zeazbcdebcdrttw")

