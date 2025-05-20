from collections import deque

def find_shortest_path(start_station, end_station, metro_lines):
    # Funzione per trovare il percorso più breve tra due stazioni
    graph = build_graph(metro_lines)
    return bfs_shortest_path(graph, start_station, end_station)

def build_graph(metro_lines):
    # Crea una rappresentazione del grafo delle stazioni
    graph = {}
    for line, stations in metro_lines.items():
        for i in range(len(stations) - 1):
            if stations[i] not in graph:
                graph[stations[i]] = []
            if stations[i + 1] not in graph:
                graph[stations[i + 1]] = []
            graph[stations[i]].append(stations[i + 1])
            graph[stations[i + 1]].append(stations[i])
    return graph

def bfs_shortest_path(graph, start, end):
    # Implementazione della ricerca BFS per il percorso più breve
    if start == end:
        return [start]

    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        station = path[-1]

        if station in visited:
            continue

        for neighbor in graph.get(station, []):
            new_path = list(path)
            new_path.append(neighbor)
            queue.append(new_path)

            if neighbor == end:
                return new_path

        visited.add(station)

    return None

def calculate_stops(path):
    # Funzione per calcolare il numero di fermate e i cambi di linea
    total_stops = len(path) - 1
    line_stops = {}
    changes = []

    return total_stops, line_stops, changes