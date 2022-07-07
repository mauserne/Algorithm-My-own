//오븐 시계
//https://www.acmicpc.net/problem/2525

const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

var time = input[0].split(' ');
var h = parseInt(time[0]), m = parseInt(time[1]);

var req = parseInt(input[1]);

var req_h = parseInt(req/60), req_m = req%60

m += req_m;

if (m>59){
    h++
    m -= 60
}

h += req_h;

if (h> 23){
    h %= 24
}

console.log(h,m)