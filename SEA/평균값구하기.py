T = int(input())
for test_case in range(1, T + 1):
    data=list(map(int, input().split()))
    result=0
    """
    for i in range(len(data)):
        result+=data[i]
    result/=len(data)    
    """
    # for문 안쓰고 sum()함수를 써서 더하기
    # 나누기 한번에 계산
    result=sum(data)/len(data)

    result=round(result)
    print('#%d %d' % (test_case, result))