//A+B - 5
//https://www.acmicpc.net/problem/10952

const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

var result = '';

for (var i in input){
    var [a,b] = input[i].split(' ').map(el=>+el);
    if (a == 0 && b == 0){
        break
    }
    result += a+b+'\n'
}
console.log(result)