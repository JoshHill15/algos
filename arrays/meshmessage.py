# You wrote a trendy new messaging app, MeshMessage, to get around flaky cell phone coverage.

# Instead of routing texts through cell towers, your app sends messages via the phones of nearby users, passing each message along from one phone to the next until it reaches the intended recipient. (Don't worry—the messages are encrypted while they're in transit.)

# Some friends have been using your service, and they're complaining that it takes a long time for messages to get delivered. After some preliminary debugging, you suspect messages might not be taking the most direct route from the sender to the recipient.

# Given information about active users on the network, find the shortest route for a message from one user (the sender) to another (the recipient). Return a list of users that make up this route.

# There might be a few shortest delivery routes, all with the same length. For now, let's just return any shortest route.

# Your network information takes the form of a dictionary mapping username strings to a list of other users nearby:

from collections import deque
network = {
    'Min': ['William', 'Jayden', 'Omar'],
    'William': ['Min', 'Noam'],
    'Jayden': ['Min', 'Amelia', 'Ren', 'Noam'],
    'Ren': ['Jayden', 'Omar'],
    'Amelia': ['Jayden', 'Adam', 'Miguel'],
    'Adam': ['Amelia', 'Miguel', 'Sofia', 'Lucas'],
    'Miguel': ['Amelia', 'Adam', 'Liam', 'Nathan'],
    'Noam': ['Nathan', 'Jayden', 'William'],
    'Omar': ['Ren', 'Min', 'Scott']
}
sender = "Jayden"
recip = "Adam"

sender2 = "dfsdf"
recip2 = "Adam"
# Python 2.7
# For the network above, a message from Jayden to Adam should have this route:

#   ['Jayden', 'Amelia', 'Adam']


def mesh(network, sender, recipient):
    if sender not in network or recipient not in network:
        return "Error: please input valid sender and recipient."

    q = [[sender]]

    while len(q) > 0:
        path = q.pop(0)
        person = path[-1]

        for new_person in network[person]:
            new_path = list(path)
            new_path.append(new_person)
            q.append(new_path)

            if new_path[-1] == recipient:
                return new_path

    return "no path"


print(mesh(network, sender2, recip2))


def reconstruct_path(previous_nodes, start_node, end_node):
    reversed_shortest_path = []

    # Start from the end of the path and work backwards
    current_node = end_node
    while current_node:
        reversed_shortest_path.append(current_node)
        current_node = previous_nodes[current_node]

    # Reverse our path to get the right order
    reversed_shortest_path.reverse()  # flip it around, in place
    return reversed_shortest_path  # no longer reversed


def bfs_get_path(graph, start_node, end_node):
    if start_node not in graph:
        raise Exception('Start node not in graph')
    if end_node not in graph:
        raise Exception('End node not in graph')

    nodes_to_visit = deque()
    nodes_to_visit.append(start_node)

    # Keep track of how we got to each node
    # We'll use this to reconstruct the shortest path at the end
    # We'll ALSO use this to keep track of which nodes we've
    # already visited
    how_we_reached_nodes = {start_node: None}

    while len(nodes_to_visit) > 0:
        current_node = nodes_to_visit.popleft()

        # Stop when we reach the end node
        if current_node == end_node:
            return reconstruct_path(how_we_reached_nodes, start_node, end_node)

        for neighbor in graph[current_node]:
            if neighbor not in how_we_reached_nodes:
                nodes_to_visit.append(neighbor)
                how_we_reached_nodes[neighbor] = current_node

    # If we get here, then we never found the end node
    # so there's NO path from start_node to end_node
    return None


print(bfs_get_path(network, sender, recip))
