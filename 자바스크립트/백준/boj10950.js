//A+B - 3 
//https://www.acmicpc.net/problem/10950

const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

for (var i = 1; i <= Number(input[0]); i++){
    [a,b] = input[i].split(' ').map(el=>+el);
    console.log(a+b);
}
