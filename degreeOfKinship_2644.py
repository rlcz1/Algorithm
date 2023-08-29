# A에서 B로 가는 최단 거리
N = int(input())
A, B = map(int, input().split(' '))
m = int(input())

graph_list = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
result = []  # 최단 거리를 저장할 리스트

for _ in range(m):
    x, y = map(int, input().split())
    graph_list[x].append(y)
    graph_list[y].append(x)

# 시작노드 v, 거리 cnt
def dfs(v, cnt):
    cnt += 1
    visited[v] = True  # v 방문처리

    if v == B:  # v가 목표와 같다면
        result.append(cnt)

    for i in graph_list[v]:
        if not visited[i]:  # 아직 방문하지 않았다면 재호출
            dfs(i, cnt)

dfs(A, 0)

if len(result) == 0:
    print(-1)
else:
    print(result[0] - 1)
