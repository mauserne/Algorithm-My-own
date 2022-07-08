//두 수 비교하기
//https://www.acmicpc.net/problem/1330

var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().split(' ');
var a = parseInt(input[0]), b = parseInt(input[1]);

if (a < b){
    console.log('<')
} else if (a > b){
    console.log('>')
} else {
    console.log('==')
}