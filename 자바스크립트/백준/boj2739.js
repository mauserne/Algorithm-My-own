//구구단
//https://www.acmicpc.net/problem/2739

const fs = require('fs');
const input = parseInt(fs.readFileSync('/dev/stdin').toString());

for (var i=1; i < 10; i++){
    console.log(input,'*',i,'=',input*i)
}