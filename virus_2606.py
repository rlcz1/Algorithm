from collections import deque

# graph_list = {
#     1: {2, 5},
#     2: {3},
#     3: {},
#     4: {7},
#     5: {2, 6},
#     6: {}
# }

N = int(input())
C = int(input())

graph_list = {}

for i in range(C):
    a, b = map(int, input().split(' '))
    keys = graph_list.keys()
    if a in keys:
        graph_list[a].add(b)
    else:
        graph_list[a] = {b}

root_node = 1

print(graph_list)


def bfs(graph, root):
    visited = []  # 방문 했던 노드
    queue = deque([root])  # 방문 할 노드(시작 노드)

    while queue:  # 더이상 방문할 노드가 없을 때까지
        n = queue.popleft()  # 맨앞의 노드를 꺼냄
        if n not in visited:  # 해당 노드가 방문 리스트에 없다면
            visited.append(n)  # 방문 리스트에 추가
            queue += graph[n] - set(visited)  # 해당 노드의 자식 노드들을 큐에 추가

    return visited


print(bfs(graph_list, root_node))
