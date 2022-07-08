//시험 성적
//https://www.acmicpc.net/problem/9498

var fs = require('fs');
var score = fs.readFileSync('/dev/stdin').toString();

if (score >= 90){
    console.log('A')
} else if (score >= 80){
    console.log('B')
} else if (score >= 70){
    console.log('C')
} else if (score >= 60){
    console.log('D')
} else {
    console.log('F')
}