valid_graph = {
    "data": [
        {"source": "A", "target": "B", "distance": 6},
        {"source": "A", "target": "E", "distance": 4},
        {"source": "B", "target": "A", "distance": 6},
        {"source": "B", "target": "C", "distance": 2},
        {"source": "B", "target": "D", "distance": 4},
        {"source": "C", "target": "B", "distance": 3},
        {"source": "C", "target": "D", "distance": 1},
        {"source": "C", "target": "E", "distance": 7},
        {"source": "D", "target": "B", "distance": 8},
        {"source": "E", "target": "B", "distance": 5},
        {"source": "E", "target": "D", "distance": 7},
    ]
}


invalid_graph = {
    "data": [
        {"source": "A", "target": "A", "distance": 6},
        {"source": "A", "target": "B", "distance": 6},
        {"source": "A", "target": "B", "distance": 6},
        {"source": "A", "target": "E", "distance": 4},
        {"source": "B", "target": "A", "distance": 6},
        {"source": "B", "target": "C", "distance": 2},
        {"source": "B", "target": "D", "distance": 4},
        {"source": "C", "target": "B", "distance": 3},
        {"source": "C", "target": "D", "distance": 1},
        {"source": "C", "target": "E", "distance": 7},
        {"source": "D", "target": "B", "distance": 8},
        {"source": "E", "target": "B", "distance": 5},
        {"source": "E", "target": "D", "distance": 7},
    ]
}

valid_graph_all_routes_no_maxstops = {
    "data": [
        {"source": "A", "target": "B", "distance": 5},
        {"source": "B", "target": "C", "distance": 4},
        {"source": "C", "target": "D", "distance": 8},
        {"source": "D", "target": "C", "distance": 8},
        {"source": "D", "target": "E", "distance": 6},
        {"source": "A", "target": "D", "distance": 5},
        {"source": "C", "target": "E", "distance": 2},
        {"source": "E", "target": "B", "distance": 3},
        {"source": "A", "target": "E", "distance": 7},
    ]
}

valid_graph_all_routes_response_no_maxstops = {
    "routes": [
        {"route": "ABC", "stops": "2"},
        {"route": "ADC", "stops": "2"},
        {"route": "ADEBC", "stops": "4"},
        {"route": "AEBC", "stops": "3"},
    ]
}
