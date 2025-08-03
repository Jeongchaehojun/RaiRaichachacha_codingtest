#2025.08.03
#s2
#이진 탐색 알고리즘 예제 찾은거임
#한 줄로 이어진 나무에서 높이 H 이상을 자르면 위에 원래 나무 높이 - H 만큼 남겠죠?
#그것들 다 합쳐서 M이 되는지 확인하고 끝내면 되겠죠

n, m = map(int, input().split()) #나무 수, 필요한 M길이
trees = list(map(int, input().split()))

start = 0 #최소 절단기 높이
end = max(trees) #최대 절단기 높이

result = 0 #최종 절단기 높이

while start <= end:
    mid = (start+end) // 2
    total = 0 #나무 자른 것들 합칠 것

    for tree in trees:
        if tree > mid:
            total += tree - mid

    if total >= m:
        #자른 것들 다 합쳤더니 m보다 크면 H가 높아져도 됨
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
#브루트포스로 풀면 시간초과가 남.. 그래서 이진탐색하려고 mid 갈기는거임
#근데 이렇게 해도 시간초과가 나버리네;; 근데 파이썬이 아니라 pypy3로 제출하면 성공;;