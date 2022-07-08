//A+B - 4
//https://www.acmicpc.net/problem/10951

const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

var result = '';

for (var i in input){
    var [a,b] = input[i].split(' ').map(el=>+el);
    result += a+b+'\n';
}
console.log(result)