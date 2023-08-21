from collections import deque

N = int(input())
C = int(input())

graph_list = {}

for i in range(C):
    a, b = map(int, input().split(' '))
    if a in graph_list:
        graph_list[a].add(b)
    else:
        graph_list[a] = {b}

    if b in graph_list:
        graph_list[b].add(a)
    else:
        graph_list[b] = {a}

root_node = 1


def bfs(graph, root):
    visited = set()  # 방문한 노드 집합으로 변경
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.add(n)  # 방문한 노드 집합에 추가
            if n in graph:
                queue.extend(graph[n] - visited)  # 차집합 연산을 통해 이미 방문한 노드는 큐에 추가하지 않도록 함

    return visited


result = bfs(graph_list, root_node)
print(len(result) - 1)  # 1번 컴퓨터는 제외
