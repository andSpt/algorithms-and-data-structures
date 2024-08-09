import sys


sys.setrecursionlimit(40000)

N = int(input())
M = map(int, input().split())

graph = {i: list() for i in range(N)}
root = None
for child, parent in enumerate(M):
    if parent != -1:
        graph[parent].append(child)
    else:
        root = child

def height_tree(vertex):
    height = 1
    for children in graph[vertex]:
        height = max(height, 1 + height_tree(children))
    return height

print(height_tree(root))