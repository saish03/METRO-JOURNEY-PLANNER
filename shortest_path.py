import heapq

def dijkstra(graph, start, end):
    queue = [(0, start, [])]
    visited = set()

    while queue:
        cost, node, path = heapq.heappop(queue)

        if node in visited:
            continue

        visited.add(node)
        path = path + [node]

        if node == end:
            return cost, path

        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                total_cost = cost + graph[node][neighbor]["weight"]
                heapq.heappush(queue, (total_cost, neighbor, path))

    return float("inf"), []
