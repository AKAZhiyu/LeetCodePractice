"""
# Definition for a Node.

"""
from collections import deque
from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    #dfs
    def cloneGraph_dfs(self, node: Optional['Node']) -> Optional['Node']:
        node_dict = {}

        def dfs(node):
            if not node:
                return None

            if node in node_dict:
                return node_dict[node]

            new_node = Node(node.val, [])
            node_dict[node] = new_node

            for neighbor in node.neighbors:
                new_node.neighbors.append(dfs(neighbor))

            return new_node

        return dfs(node)

    # bfs
    def cloneGraph_bfs(self, node: Optional['Node']) -> Optional['Node']:
        node_dict = {}

        def bfs(node):
            if not node:
                return

            queue = deque([node])
            new_node = Node(node.val, [])
            node_dict[node] = new_node

            while queue:
                temp = queue.popleft()
                for neighbor in temp.neighbors:
                    if neighbor not in node_dict:
                        node_dict[neighbor] = Node(neighbor.val, [])
                        queue.append(neighbor)
                    node_dict[temp].neighbors.append(node_dict[neighbor])

            return new_node

        return bfs(node)