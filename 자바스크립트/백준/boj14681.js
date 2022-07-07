//사분면 고르기
//https://www.acmicpc.net/problem/14681

const fs = require('fs');
const input = fs.readFileSync(0).toString().split('\n');

let x = parseInt(input[0]), y = parseInt(input[1]);

if ( y > 0 ){
    if ( x > 0 ){
        console.log(1);
    } else {
        console.log(2);
    }
} else {
    if ( x > 0 ){
        console.log(4);
    } else {
        console.log(3);
    }
}