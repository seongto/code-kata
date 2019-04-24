//*문제
//s는 여러 괄호들로 이루어진 String 인자입니다.
//s가 유효한 표현인지 아닌지 true/false로 반환해주세요.
//
//종류는 '(', ')', '[', ']', '{', '}' 으로 총 6개 있습니다.
//아래의 경우 유효합니다.
//한 번 괄호를 시작했으면, 같은 괄호로 끝내야 한다.
//괄호 순서가 맞아야 한다.
//괄호의 중첩은 허용하나 특정 괄호안에서 시작한 괄호는 부모 괄호 안에서 끝내야 한다.
//
//예를 들어 아래와 같습니다.
//
//s = "()"
//return true
//
//s = "()[]{}"
//return true
//
//s = "(]"
//return false
//
//s = "([)]"
//return false
//
//s = "{[]}"
//return true


function isValid(s) {
  let str = s.slice();
  let length = s.length;

  for (let i = 0; i < length/2; i++){
    for (let j = 0; j < length-1; j++){
      let fair = str[j]+str[j+1];
      console.log(fair);
      if ( (fair === "()") || (fair === "{}") || (fair === "[]")){
        str= str.replace(str[j+1], "");
        str= str.replace(str[j], "");
      }
    }  
  }
  
  if (str === "") {
    return true
  } else {
    return false
  }  
}

