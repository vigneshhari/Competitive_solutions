import decimal
inf = decimal.Decimal("Infinity")

def answer(entrances, exits, path):
    transform(entrances, exits, path)
    flow = 0
    length = len(path)
    flows = [[0 for i in range(length)] for j in range(length)]
    start = 0
    end = length - 1
    while True:
        ap_flow, parents = bfs(start, end, path, flows)
        if ap_flow == 0:
            break
        flow += ap_flow
        v = end
        while v != start:
            u = parents[v]
            flows[u][v] += ap_flow
            flows[v][u] -= ap_flow
            v = u
    return flow

def bfs(start, end, path, flows):
    global inf
    length = len(path)
    parents = [-1] * length
    parents[start] = -2
    queue = []
    queue.append(start)
    while queue and parents[end] == -1:
        u = queue.pop(0)
        for v in range(length):
            cf = path[u][v] - flows[u][v]
            if cf > 0 and parents[v] == -1:
                queue.append(v)
                parents[v] = u
    if parents[end] == -1:
        return 0, parents
    v = end
    delta = inf
    while v != start:
        u = parents[v]
        cf = path[u][v] - flows[u][v]
        delta = min(delta, cf)
        v = u
    return delta, parents

def transform(entrances, exits, path):
    global inf
    length = len(path)
    entrances = [i + 1 for i in entrances]
    exits = [i + 1 for i in exits]
    for row in path:
        row.insert(0, 0)
        row.append(0)
    start_row = [0] * (length + 2)
    for i in entrances:
        start_row[i] = inf
    path.insert(0, start_row)
    end_row = [0] * (length + 2)
    for i in exits:
        path[i][-1] = inf
    path.append(end_row)
    return entrances, exits, path