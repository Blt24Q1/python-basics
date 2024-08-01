# Operator
# 기본적으로 하나의 py 파일은 그 자체가 모듈
def arith_oper():
    print("===== 산술 연산")
    print(7/3)  # 파이썬 3 -> int / int -> float
    print(7//3) # 정수 나눗셈의 몫 연산자 //
    print(7%3)  # 정수 나눗셈의 나머지 연산자

    # 나눗셈의 몫과 나머지 동시에 구함
    print(divmod(7, 3)) # -> (2, 1) : Tuple

    print("7/3의 몫:", divmod(7, 3)[0]) # 7/3의 몫
    print("7/3의 나머지:", divmod(7, 3)[1]) # 7/3의 나머지
    
    print(7**3) # 지수승: 7의 3제곱
    print(pow(7, 3)) # 지수 함수: 7의 3제곱


if __name__ == "__main__":
    # 다른 모듈로 import 되는 경우 __name__ == "python_basics"
    # 직접 실행될 경우(최상위 모듈일 경우) __name__ == "__main__"
    arith_oper()