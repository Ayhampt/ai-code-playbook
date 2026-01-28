graph = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'Q', 'SA'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW','T'],
    'T': ['V']
}


def is_valid_coloring(graph,color):
    for region in graph:
        if region not in color:
            return False
        for neighbor in graph[region]:
            if neighbor in color and color[region] == color[neighbor]:
                return False
    return True

def greedy_coloring(graph):
    coloring = {}
    for region in graph:
        used_colors = set()
        for neighbor in graph[region]:
            if neighbor in coloring:
                used_colors.add(coloring[neighbor])
        color = 0
        while color in used_colors:
            color += 1
        coloring[region] = color
    return  coloring

result = greedy_coloring(graph)
print(" Red=0,  Green=1,  Blue=2")
print("Coloring",result)
print("Valid?", is_valid_coloring(graph, result))
print("Colors used:", len(set(result.values())))