import matplotlib.pyplot as plt

def dijkstra(network, start, end):
    import heapq
    queue = []
    heapq.heappush(queue, (0, start, [start]))
    visited = set()
    while queue:
        cost, node, path = heapq.heappop(queue)
        if node == end:
            return cost, path
        if node in visited:
            continue
        visited.add(node)
        for neighbor, edge_cost in network[node].items():
            if neighbor not in visited:
                heapq.heappush(queue, (cost + edge_cost, neighbor, path + [neighbor]))
    return float("inf"), []

def visualize_network(network, optimal_routes):
    # Assign coordinates to each node for visualization
    node_positions = {
        "Warehouse": (0, 0),
        "A": (1, 2),
        "B": (-1, 2),
        "C": (0, 4),
        "D": (2, 4),
        "E": (1, 6)
    }
    fig, ax = plt.subplots(figsize=(7, 7))
    # Draw all edges in light gray
    for node, neighbors in network.items():
        for neighbor in neighbors:
            x_values = [node_positions[node][0], node_positions[neighbor][0]]
            y_values = [node_positions[node][1], node_positions[neighbor][1]]
            ax.plot(x_values, y_values, color="lightgray", zorder=1)
    # Draw optimal routes in color
    colors = ["red", "blue", "green", "orange", "purple", "brown"]
    for idx, route in enumerate(optimal_routes):
        for i in range(len(route) - 1):
            n1, n2 = route[i], route[i + 1]
            x_values = [node_positions[n1][0], node_positions[n2][0]]
            y_values = [node_positions[n1][1], node_positions[n2][1]]
            ax.plot(x_values, y_values, color=colors[idx % len(colors)], linewidth=3, zorder=2)
    # Draw nodes
    for node, (x, y) in node_positions.items():
        ax.scatter(x, y, s=300, color="white", edgecolor="black", zorder=3)
        ax.text(x, y, node, fontsize=12, ha="center", va="center", zorder=4)
    ax.set_title("Transportation Network with Optimal Delivery Routes")
    ax.axis("off")
    plt.show()

def optimize_routes(network, delivery_locations):
    route_summaries = []
    optimal_routes = []
    total_cost = 0
    max_cost = -1
    most_expensive_location = None
    for location in delivery_locations:
        cost, route = dijkstra(network, "Warehouse", location)
        route_summaries.append((location, route, cost))
        optimal_routes.append(route)
        total_cost += cost
        if cost > max_cost:
            max_cost = cost
            most_expensive_location = location
    summary_lines = []
    for location, route, cost in route_summaries:
        summary = f"Location: {location}, Optimal Route: {' -> '.join(route)}, Cost: {cost}"
        summary_lines.append(summary)
    summary_text = "\n".join(summary_lines)
    total_cost_text = f"Total transportation cost: {total_cost}"
    most_expensive_text = f"Most expensive location to reach: {most_expensive_location} (Cost: {max_cost})"
    print(summary_text)
    print(total_cost_text)
    print(most_expensive_text)
    visualize_network(network, optimal_routes)

# Sample data
network = {
    "Warehouse": {"A": 4, "B": 2},
    "A": {"Warehouse": 4, "C": 3, "D": 2},
    "B": {"Warehouse": 2, "C": 1},
    "C": {"A": 3, "B": 1, "D": 4, "E": 2},
    "D": {"A": 2, "C": 4, "E": 1},
    "E": {"C": 2, "D": 1}
}
delivery_locations = ["A", "C", "D", "E"]

optimize_routes(network, delivery_locations)
