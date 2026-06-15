import heapq

# Campus Map (Graph Representation)
campus_graph = {
    "Library": {
        "Admin": 50,
        "Hostel": 80
    },

    "Admin": {
        "Library": 50,
        "C Block": 70,
        "Auditorium": 40
    },

    "Hostel": {
        "Library": 80,
        "C Block": 40
    },

    "Auditorium": {
        "Admin": 40,
        "C Block": 30
    },

    "C Block": {
        "Admin": 70,
        "Hostel": 40,
        "Auditorium": 30
    }
}


# Heuristic Values (Estimated distance to goal)
heuristic = {
    "Library": 100,
    "Admin": 60,
    "Hostel": 50,
    "Auditorium": 20,
    "C Block": 0
}


def a_star(graph, start, goal):

    priority_queue = []
    heapq.heappush(priority_queue, (0, start))

    came_from = {}
    g_cost = {node: float('inf') for node in graph}
    g_cost[start] = 0

    while priority_queue:

        current_f, current_node = heapq.heappop(priority_queue)

        if current_node == goal:

            path = []

            while current_node in came_from:
                path.append(current_node)
                current_node = came_from[current_node]

            path.append(start)
            path.reverse()

            return path, g_cost[goal]

        for neighbor, distance in graph[current_node].items():

            new_cost = g_cost[current_node] + distance

            if new_cost < g_cost[neighbor]:

                g_cost[neighbor] = new_cost

                f_cost = new_cost + heuristic[neighbor]

                heapq.heappush(
                    priority_queue,
                    (f_cost, neighbor)
                )

                came_from[neighbor] = current_node

    return None, None


# Main Program
print("\n===== Intelligent Campus Navigation Assistant =====\n")

print("Available Locations:")
for location in campus_graph:
    print("-", location)

source = input("\nEnter Source Location: ")
destination = input("Enter Destination Location: ")

if source not in campus_graph or destination not in campus_graph:
    print("\nInvalid Location Entered!")

else:
    path, distance = a_star(
        campus_graph,
        source,
        destination
    )

    if path:
        print("\nOptimal Path Found:")
        print(" -> ".join(path))

        print(f"\nTotal Distance: {distance} meters")

    else:
        print("\nNo Path Found!")
