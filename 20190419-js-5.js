// *문제
// strs은 단어가 담긴 배열입니다.
// 공통된 시작 단어(prefix)를 반환해주세요.

// 예를 들어
// strs = ['start', 'stair', 'step']
// return은 'st'

// strs = ['start', 'wework', 'today']
// return은 ''

// --------------------------------------------

// *모법답안

// function getPrefix(strs) {
//     if (strs.length === 0) return ''; 
//     let prefix = strs[0];
//     for (let i = 1; i < strs.length; i++) {
//         while (strs[i].indexOf(prefix) !== 0) {
//             prefix = prefix.substring(0, prefix.length - 1);
//         }
//     }
//     return prefix;
// }

// --------------------------------------------

// 나의 코드

function getPrefix(strs) {
  let long = 0;
  let prefix = "";
  let check = false;
  for (let i = 0; i < strs.length; i++){
    if ( strs[i].length > long ){
      long = strs[i].length
    } 
  }
  for (let i = 0; i < long ; i++){
    console.log(check)
    let match = strs[0][i];
    for (let j = 0; j < strs.length; j++){
      if ( match !== strs[j][i] ){
        check = false;
        break;
      } else {
        check = true;
      }
    }
    if (check){
      console.log(check)
      prefix = prefix + match;
      check = false;
    }
    console.log(check)
  }
  return prefix;
}

getPrefix(['start', 'stair', 'step']);

// 나의 답 돌아보기
// 모법답안을 보고 신선한 충격이다 정말... 뭐든 반대로 생각하는 기분...
// 같은 걸 체크하는게 아니라 없는 걸 체크하고...
// 앞에서부터 쌓아가는게 아니라 뒤에서부터 잘라가고...
// 와... 대박...


