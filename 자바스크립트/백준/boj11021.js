//A+B - 7
//https://www.acmicpc.net/problem/11021

const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const T = Number(input[0]);
var result = '';

for (var i = 1; i <= T; i++){
    var [a,b] = input[i].split(' ').map(el=>+el);
    result += `Case #${i}: ${a+b}\n`
}
console.log(result);