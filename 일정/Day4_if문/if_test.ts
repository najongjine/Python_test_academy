/**
 * 타입스크립트
 */
let dummy1=false

if(dummy1){
    // 타입스크립트에서 string interpolation은 back tick을 사용
    console.log(`dummy 의 값: ${dummy1}`)
}
else if(!dummy1){
    console.log(`else if block`)
}else{
    console.log(`else`)
}