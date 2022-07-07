//알람 시계
//https://www.acmicpc.net/problem/2884
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split(' ');

var h = parseInt(input[0]), m = parseInt(input[1]);

if (m >= 45){
    console.log(h, m-45)
} else {
    if (h == 0){
        console.log(23, 60+m-45)
    } else {
        console.log(h-1, 60+m-45)
    }
}