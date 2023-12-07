#!/usr/bin/python3

def canUnlockAll(boxes):
    def dfs(box_index, visited):
        visited[box_index] = True

        for key in boxes[box_index]:
            if not visited[key]:
                dfs(key, visited)

    n = len(boxes)
    visited = [False] * n
    dfs(0, visited)

    return all(visited)

# Example usage:
boxes = [
    [1],      # Box 0 has key 1
    [2],      # Box 1 has key 2
    [3],      # Box 2 has key 3
    []        # Box 3 has no key
]

result = canUnlockAll(boxes)
print(result)

