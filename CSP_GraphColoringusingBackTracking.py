graph = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}


def is_valid_color(region, color, coloring, graph):
    for neighbor in graph[region]:
        if neighbor in coloring and coloring[neighbor] == color:
            return False
    return True


def coloring_by_backtracking(regions, colors, coloring, graph, index):
    if index == len(regions):
        return True
    region = regions[index]
    for color in colors:
        if is_valid_color(region, color, coloring, graph):
            coloring[region] = color
            if coloring_by_backtracking(regions, colors, coloring, graph, index + 1):
                return True
            del coloring[region]
    return False


regions = list(graph.keys())
colors = ['red', 'green', 'blue']
coloring = {}

if coloring_by_backtracking(regions, colors, coloring, graph, 0):
    print("Valid coloring found:")
    print(coloring)
else:
    print("No valid coloring exists")