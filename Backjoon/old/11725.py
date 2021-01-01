#Ex_11725
# tree
import sys
node = int(input())
node_graph = [ [] for _ in range(node + 1)]
parent = [ [] for _ in range(node + 1)]

#트리를 그래프 형태로 생성

for _ in range(node - 1):
    i, j = map(int, sys.stdin.readline().split())
    node_graph[i].append(j)
    node_graph[j].append(i)

#DFS
def dfs(graph,start,parent_list):
    stack = [start]

    while stack:
        node = stack.pop()
        for i in graph[node]:
            parent_list[i].append(node) # visited_list
            stack.append(i)             # next parent node
            graph[i].remove(node)       # visited.remove
    return parent_list

# dfs[1] : root's parent
# dfs[2] start!
for i in list(dfs(node_graph, 1, parent))[2:]:
    print(i[0])



