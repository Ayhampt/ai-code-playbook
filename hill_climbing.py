heuristic = {
    'A': 5,
    'B': 6,
    'C': 4,
    'D': 3,
    'E': 3,
    'F': 1,
    'G': 0
}
tree = {
    'A': ['B','C'],
    'B': ['D'],
    'C': ['E'],
    'D': ['F','G'],
    'E': ['G'],
    'F': ['G'],
    'G': []
}
def hill_climbing(start,goal):
    current = start
    path = [current]
    while current != goal:
        neighbors = tree[current]
        if not neighbors:
            break
        next_node = min(neighbors,key=lambda n:heuristic[n])
        if heuristic[next_node] < heuristic[current]:
            current = next_node
            path.append(current)
        else:
            break
    return path
result = hill_climbing('A','G')
print('Hill climbing Path :',"->".join(result))