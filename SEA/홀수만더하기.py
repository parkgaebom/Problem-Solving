t=int(input())
for test_case in range(1, t+1):
    data=list(map(int, input().split()))#데이터 입력
    result=0 #결과 값
    for i in range(len(data)): #리스트의 길이만큼
        if data[i]%2==1: #홀수면
            result+=data[i] #더하기
    print('#%d %d'% (test_case, result)) #결과 출력


