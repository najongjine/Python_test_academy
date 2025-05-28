/**
 * 자바 스크립트 = 파이썬처럼 아무거나 막 담음
 * 근데 파이썬보다 더 무식하게 잘담음
 * 이게 장점이자 단점
 *
 * 그래서 데이터 구조가 복잡하면,
 * 거기에 있는값을 꺼내거나 연산할때 에러검출이 하나도 안됨
 *
 * 클라이언트가 데이터를 보낼때 어떻게 보내야할까 거진 신경 안씀
 * 그냥 보내버림
 * 서버도 그냥 받아버림
 * 이게 진짜 최강임
 */
// number1=1 파이썬 스타일
let number = 1.121;
let string1 = "dfdfd";
let bBool = true;
let jObj = {};
// a["뭐뭐"]     
jObj.a = "a";
jObj.func1 = () => {
  console.log("나는 func1");
};
jObj.func1();
let jObj={
    response:true
    document:{
        items:{
            item:{
                subclass:{
                    items:{

                    }
                }
            }
        }
    }
}

/**
 * 클라이언트가 데이터를 보낼때는 클라이언트마다 어떻게 타입이 올지 다다름
 * 그런데 그냥 수학연산 때리면, 이거 값 어떻게 나올지 모름
 */
let price=queueMicrotask.pram
let 통잔잔고= 통장잔고+price 


function getRandomIntInclusive(min: number, max: number): number {
  const minCeiled = Math.ceil(min);
  const maxFloored = Math.floor(max);
  return Math.floor(Math.random() * (maxFloored - minCeiled + 1)) + minCeiled;
}



let list1 = [
  { 제품: "뭐뭐1", 가격: 1110 },
  { 제품: "뭐뭐2", 가격: 20 },
  { 제품: "뭐뭐3", 가격: 3005 },
  { 제품: "뭐뭐4", 가격: 400 },
  { 제품: "뭐뭐5", 가격: 5050 },
];

list1.sort((a, b) => a.가격 - b.가격);