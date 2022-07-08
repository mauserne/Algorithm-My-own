//별 찍기 - 2
//https://www.acmicpc.net/problem/2439

const fs = require('fs');
const N = Number(fs.readFileSync('/dev/stdin').toString());

star = ''
result = ''

for (var i = 1; i <= N; i++){
    star += '*';
    blank = '';
    for (var j = 1; j <= N-i; j++){
        blank += ' ';
    }
    result += blank+star+'\n';
}

console.log(result)