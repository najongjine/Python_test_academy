function getRandomIntInclusive(min: number, max: number): number {
  const minCeiled = Math.ceil(min);
  const maxFloored = Math.floor(max);
  return Math.floor(Math.random() * (maxFloored - minCeiled + 1)) + minCeiled;
}

let number1 = getRandomIntInclusive(0, 99999);
let result = ""; // 여기 result
if (number1 % 2 == 0) {
  let result = "짝수입니다"; // 여기 result scope 이 다름
} else {
  let result = "홀수입니다";
}
