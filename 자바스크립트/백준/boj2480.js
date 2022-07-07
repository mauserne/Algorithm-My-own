//주사위 세개
//https://www.acmicpc.net/problem/2480

const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split(' ').map(el=>+el);

const [a, b, c] = input;
const obj = {};


for (var i in input){
    if (input[i] in obj){
        obj[input[i]]++
    } else {
        obj[input[i]] = 1
    }
}

const len_obj = Object.keys(obj).length;

if (len_obj == 1){
    console.log(10000+input[0]*1000)
} else if (len_obj == 2){
    for (var i in obj){
        if (obj[i]==2){
            console.log(1000+i*100)
        }
    }
} else {
    console.log(Math.max(...input)*100)
}