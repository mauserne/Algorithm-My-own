//빠른 A+B
//https://www.acmicpc.net/problem/15552

const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const T = Number(input[0]);
var result = '';

for (var i = 1; i <= T; i++){
    var [a,b] = input[i].split(' ').map(el=>+el);
    result += a + b +'\n'
}
console.log(result);

// 하나씩 출력하면 시간이 오래걸려서 계산한 결과를 모아뒀다가 마지막에 출력한다.