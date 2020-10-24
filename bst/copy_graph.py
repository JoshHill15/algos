from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def traverse(self, node, seen):
        for n in node.neighbors:
            if n not in seen:
                seen[n] = n.neighbors
                self.traverse(n, seen)

    def trav(self, node, seen):
        q = deque()
        q.append(node)

        while q:
            curr = q.popleft()

            if curr not in seen:
                seen[curr] = curr.neighbors

                for n in curr.neighbors:
                    if n not in seen:
                        q.append(n)

    def cloneGraph(self, node: 'Node') -> 'Node':
        seen = {}
        self.trav(node, seen)
        res = None
        first = True

        for key in seen:
            new_node = Node(key.val)
            if first:
                res = new_node
                first = False

            for n in seen[key]:
                new_neighbor = Node(n.val)
                new_node.neighbors.append(new_neighbor)

            print(new_node.val, new_node.neighbors)

        print(res.val)
        return res

    def cloneGraph2(self, node):
        memo = {}

        def clone(node):
            if node not in memo:
                c = memo[node] = Node(node.val)
                c.neighbors = map(clone, node.neighbors)
                v = c.neighbors
                x = list(c.neighbors)
                for n in x:
                    print(n.val)

            return memo[node]

        return node and clone(node)

    def cloneGraph3(self, node):  # BFS
        if not node:
            return node

        m = {node: Node(node.val)}
        q = deque()
        q.append(node)

        while q:
            n = q.popleft()
            for neigh in n.neighbors:
                if neigh not in m:
                    q.append(neigh)
                    m[neigh] = Node(neigh.val)

                m[n].neighbors.append(m[neigh])

        return m[node]


#             for val in seen[key]: print(val.val)
#             print("next")
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors.append(node2)
node1.neighbors.append(node4)

node2.neighbors.append(node1)
node2.neighbors.append(node3)

node3.neighbors.append(node2)
node3.neighbors.append(node4)

node4.neighbors.append(node1)
node4.neighbors.append(node3)


x = Solution().cloneGraph3(node1)
print(x.val)
