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

/**
 *  primitive : 숫자, 문자, bool 이런건 타입이 자동으로 정해짐
 *  나머지는 내가 정해주면됨
 *  근데 타입 정해주기 귀찬으면 any 씀
 */

export interface KakaoPlace {
  id: string;
  place_name: string;
  address_name: string;
  road_address_name: string;
  phone: string;
  category_name: string;
  category_group_code: string;
  category_group_name: string;
  x: string; // 경도 (longitude)
  y: string; // 위도 (latitude)
  distance?: string; // 선택적 필드: 거리 (미터 단위)
  place_url: string;
}

// 검색 메타데이터
export interface KakaoSearchMeta {
  total_count: number;
  pageable_count: number;
  is_end: boolean;
  same_name: {
    keyword: string;
    region: string[];
    selected_region: string;
  };
}

let anyting: KakaoSearchMeta;
