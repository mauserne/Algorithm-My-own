//윤년
//https://www.acmicpc.net/problem/2753

const fs = require('fs');
const year = parseInt(fs.readFileSync('/dev/stdin').toString());

if (year%4==0 && year%100!=0 || year%400==0){
    console.log(1)
} else {
    console.log(0)
}