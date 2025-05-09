# 퍼셉트론 클래스 정의
class Perceptron:
    def __init__(self, input_size, learning_rate=0.1):
        # 가중치와 바이어스 초기화
        self.weights = [0.0] * input_size
        self.bias = 0.0
        self.learning_rate = learning_rate

    def activation(self, x):
        # 활성화 함수: 계단 함수
        return 1 if x > 0 else 0

    def predict(self, inputs):
        # 입력과 가중치의 가중합 계산 후 활성화 함수 적용
        total = sum(w * x for w, x in zip(self.weights, inputs)) + self.bias
        return self.activation(total)

    def train(self, training_data, labels, epochs=10):
        # 주어진 데이터로 퍼셉트론 학습
        for _ in range(epochs):
            for inputs, label in zip(training_data, labels):
                print(f"입력: {inputs}, 레이블: {label}")
                prediction = self.predict(inputs)
                error = label - prediction
                # 가중치와 바이어스 업데이트
                self.weights = [
                    w + self.learning_rate * error * x
                    for w, x in zip(self.weights, inputs)
                ]
                self.bias += self.learning_rate * error


# 키워드: "무료", "당첨", "광고"
# 각 메시지를 키워드의 존재 여부로 표현
training_inputs = [
    [1, 1, 1],  # "무료 당첨 광고" -> 스팸
    [1, 0, 1],  # "무료 광고" -> 스팸
    [0, 1, 0],  # "당첨" -> 스팸
    [0, 0, 0],  # "안녕하세요" -> 일반
    [0, 0, 1],  # "광고" -> 스팸
    [1, 0, 0],  # "무료" -> 스팸
    [0, 1, 1],  # "당첨 광고" -> 스팸
    [0, 0, 0],  # "회의 일정" -> 일반
]
labels = [1, 1, 1, 0, 1, 1, 1, 0]  # 정답 레이블 목록. 스팸: 1, 일반: 0


# 퍼셉트론 생성 및 학습
perceptron = Perceptron(input_size=3)
perceptron.train(training_inputs, labels)

# 테스트 데이터
test_inputs = [
    [1, 1, 0],  # "무료 당첨" -> 예상: 스팸
    [0, 0, 0],  # "안녕하세요" -> 예상: 일반
    [0, 1, 1],  # "당첨 광고" -> 예상: 스팸
]

# 테스트 결과 출력
for inputs in test_inputs:
    result = perceptron.predict(inputs)
    print(f"입력: {inputs} => 예측 결과: {'스팸' if result == 1 else '일반'}")
