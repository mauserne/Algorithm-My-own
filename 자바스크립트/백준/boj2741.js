//N 찍기
//https://www.acmicpc.net/problem/2741

const fs = require('fs');
const N = Number(fs.readFileSync('/dev/stdin').toString());

var result = '';

for (var i = 1; i <= N; i++){
    result += i+'\n'
}

console.log(result)