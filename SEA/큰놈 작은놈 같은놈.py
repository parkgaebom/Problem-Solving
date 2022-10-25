t=int(input())
for test_case in range(1, t+1):
    """
    a=input()
    b=input()
    """
    # map(function, iterable)
    # 설명: 리스트의 요소를 지정된 함수로 처리해주는 함수
    # 사용 이유: 여러 개의 데이터를 한번에 다른 형태로 변환하기 위해 사용
    # 두번째 인자 즉 입력값들을 첫번째 인자 즉 정수형으로 저장
    a,b=map(int, input().split())

    if a>b:
        result='>'
    elif a<b:
        result='<'
    elif a==b:
        result='='

    print('#%d %c' % (test_case, result))