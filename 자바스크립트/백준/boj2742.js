//기찍 N
//https://www.acmicpc.net/problem/2742

const fs = require('fs');
const N = Number(fs.readFileSync('/dev/stdin').toString());

var result = '';

for (var i = N; i >= 1; i--){
    result += i+'\n'
}

console.log(result)