def find_all_routes(graph, start, end, max_steps=10**99, route=[]):
    route = route + [start]
    if start == end:
        return [route]
    if start not in graph:
        return []
    routes = []
    for node in graph[start]:
        if node not in route:
            new_routes = find_all_routes(graph, node, end, max_steps, route)
            for new_route in new_routes:
                routes.append(new_route)
    for route in routes:
        if len(route) > max_steps + 1:
            routes.remove(route)
    return routes


def min_route(graph, start, end, max_steps=10**99):
    routes = find_all_routes(graph, start, end, max_steps)
    min_distance = 10**99
    best_route = []
    for route in routes:
        t = sum(graph[i][j] for i, j in zip(route, route[1::]))
        if t < min_distance:
            min_distance = t
            best_route = route
    return {"distance": min_distance, "path": best_route}


def all_nodes(endpoint_graph_data):
    nodes = []
    for route in endpoint_graph_data:
        nodes.append(route["source"])
    return list(set(nodes))


def remove_duplicated_in_data(graph_data: list):
    seen = set()
    formated_json = []
    for route in graph_data:
        keys = tuple(route.items())
        if keys not in seen:
            seen.add(keys)
            formated_json.append(route)
    return formated_json


def remove_same_source_and_target(graph_data: list):
    formated_graph_data = list(
        filter(lambda route: route["source"] != route["target"], graph_data)
    )
    return formated_graph_data


def format_graph_data(endpoint_graph_data):
    formated_graph = {}
    for node in all_nodes(endpoint_graph_data):
        routes = list(
            filter(lambda route: route["source"] == node, endpoint_graph_data)
        )
        targets = []
        for route in routes:
            targets.append((route["target"], int(route["distance"])))
            formated_graph.update({route["source"]: dict(targets)})

    return formated_graph


def format_distance_to_int(graph_data):
    for route in graph_data:
        route["distance"] = int(route["distance"])
    return graph_data
