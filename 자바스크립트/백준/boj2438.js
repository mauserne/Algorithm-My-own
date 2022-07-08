//별 찍기 - 1
//https://www.acmicpc.net/problem/2438

const fs = require('fs');
const N = Number(fs.readFileSync('/dev/stdin').toString());

var star = ''
var result = ''

for (var i = 1; i <= N; i++){
    star += '*'
    result += star+'\n'
}
console.log(result)