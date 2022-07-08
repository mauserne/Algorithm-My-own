//X보다 작은 수
//https://www.acmicpc.net/problem/10871

const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const [n,x] = input[0].split(' ').map(el=>+el);
let a = input[1].split(' ').map(el=>+el);

var result = '';

for (var i in a){
    if (x > a[i]){
        result += a[i]+' '
    }
}
console.log(result)