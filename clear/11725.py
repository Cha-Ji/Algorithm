#Ex_11725
# 트리
# 그래프를 이용
# 도저히 모르겠다
def dfs(graph_list,start,parent):
    stack=[start]

    while stack:
        node=stack.pop()
        for i in graph_list[node]:
            parent[i].append(node)
            stack.append(i)
            graph_list[i].remove(node)
    return parent

import sys

node = int(sys.stdin.readline())
node_graph = [[] for _ in range(node+1)]
parent = [[] for _ in range(node+1)]

for _ in range(node - 1):
    i,j=map(int,sys.stdin.readline().split())
    node_graph[i].append(j)
    node_graph[j].append(i)

for i in list(dfs(node_graph,1,parent))[2:]:
    print(i[0])