def breadth_first_search(graph, start_node):
    visited = []
    queue = [start_node]
    while queue:
        node = queue.pop(0)
        for neighbor in graph[node]:
            if neighbor not in visited:
                print(neighbor)
                visited.append(neighbor)
                queue.append(neighbor)
    return visited

def depth_first_search(graph,start_node):
    visited = []
    stack = [start_node]
    while stack:
        node = stack.pop(0)
        print(node)
        visited.append(node)
        for child in graph[node]:
            stack.insert(0, child)
    return visited

def depth_first_search_recursive(graph, start_node):
    visited = []
    stack = [start_node]
    node = stack.pop(0)
    print(node)
    for child in graph[node]:
        stack.insert(0,child)
        depth_first_search_recursive(graph, child)

if __name__ == '__main__':
    graph = {0: [1, 2], 1: ['a', 'b'], 2: [5, 7], 'a': [], 'b': [], 5: [6], 6: [], 7: []}
    #visited_nodes=breadth_first_search(graph, 0)
    #visited_nodes = depth_first_search(graph, 0)
    visited_nodes = depth_first_search_recursive(graph, 0)
    #print(visited_nodes)