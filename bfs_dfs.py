from  collections import deque

from defer import return_value

graph = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['F'],
    'F':[]
}
def bfs(graph,start):
    visited = set()
    queue = deque([start])
    order = []
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            order.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return order

def dfs(grapg,start):
    visited = set()
    order = []
    def recursive(node):
        visited.add(node)
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not  in visited:
                recursive(neighbor)
    recursive(start)
    return order





if __name__ == "__main__":
    print("The bfs is :",bfs(graph,'A'))
    print("The bfs is :", dfs(graph, 'A'))
