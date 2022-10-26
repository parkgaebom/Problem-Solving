T = int(input())
#for test_case in range(1, T + 1): #한번 실행하기때문에 필요 없음
data=list(map(int, input().split()))
data.sort() #정렬 후
print(data[int((T-1)/2)]) #int형의 중간값 구하기(T-1)은 마지막 원소
