//합
//https://www.acmicpc.net/problem/8393

const fs = require('fs');
const n = Number(fs.readFileSync('/dev/stdin').toString());

var ans = 0;

for (var cnt = 1; cnt <= n; cnt++){
    ans += cnt
}
console.log(ans)