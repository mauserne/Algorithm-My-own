//더하기 사이클
//https://www.acmicpc.net/problem/1110

const fs = require('fs');
const input = Number(fs.readFileSync('/dev/stdin').toString());

var n = input;
var sum;
var count = 0

while (true){
    count++;

    sum = Math.floor(n / 10) + n % 10;
    n = (n % 10) * 10 + sum % 10; 

    if (n == input){
        break;
    }
}
console.log(count)