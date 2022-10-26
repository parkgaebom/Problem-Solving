T = int(input())
for test_case in range(1, T + 1):
    data=list(map(int, input().split()))
    data.sort() #오름차순으로 정렬
    # 정렬된 list에서 마지막 원소 data[-1] 즉 최대값을 출력 !!!
    print('#%d %d' % (test_case, data[-1]))