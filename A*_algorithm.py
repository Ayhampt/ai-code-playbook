heuristics = {
    'A':5,
    'B':6,
    'C':4,
    'D':3,
    'E':3,
    'F':1,
    'G':0
}
graph = {
    'A': [('B',1),('C',4)],
    'B': [('C',2),('D',3)],
    'C': [('E',5)],
    'D': [('F',2),('C',4)],
    'E': [('G',3)],
    'F': [('G',1)],
    'G': []
}

def a_star(graph,heuristics,start,goal):
    open_list = [start]
    g_cost = {start:0}
    parent = {start:None}
    while open_list:
        current = min(open_list,key=lambda x:g_cost[x]+heuristics[x])
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]
        open_list.remove(current)
        for neighbor,cost in graph[current]:
            new_g = g_cost[current]+cost
            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                parent[neighbor] = current
                open_list.append(neighbor)
    return None
path = a_star(graph,heuristics,'A','G')
print("Optimal path",path)