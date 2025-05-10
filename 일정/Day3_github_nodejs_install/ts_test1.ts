//npx tsx ts_test1.ts

let aaa:number=0
let bb:number=1121.11
let total=aaa+bb

console.log(total)

/**
 * 타입스크립트는 c# 이랑 파이썬을 섞어놓은 느낌이다.
 * 옛날 개발자들, 계산이 하나라도 오차가 있어선 안되는 작업자들이 좋아한다
 * 타입스크립트로 셋팅하면 자바스크립트도 공짜로 쓸수있다
 */

// 자바스크립트 예:
var a:any=1
a="ss"

var b:any="ss"
var b:any={}
// 자바스크립트 예: END


let jsObject:any={name:"ㅁㅂㅂ",phonenum:"010"} // javascript object
console.log(jsObject?.money)
/**
 * jsObject?.money 이렇게 ? 표를 붙이는걸 null safety 코딩이라 한다.
 */
