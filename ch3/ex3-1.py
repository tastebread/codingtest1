n, m, k = map(int, input().split()) # 3개의 자연수 입력받기

#N개의 수를 공백으로 구분하여 입력받기
number = list(map(int, input().split()))

number.sort() # 데이터 정렬

first = number[n - 1] # 가장 큰 수
second = number[n - 2]# 두 번째로 큰 수

result = 0

while True:
    for i in range(k): # 가장 큰 수를 (k)번 더하기
        if m == 0: # m 이 0이라면 탈출
            break
        result += first
        m -= 1 # 더할 때마다 1씩 빼기
    if m == 0: # m이 0이라면 반복문 탈출
        break
    result += second # 두 번째로 큰 수를 한 번 더하기
    m -= 1 #더할때마다 하나씩 빼기

print(result)
