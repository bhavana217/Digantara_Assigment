def binary_search(arr, target):
    if not isinstance(arr, list) or not all(isinstance(x, (int, float)) for x in arr):
        raise ValueError("Input array must be a list of numbers.")
    if not isinstance(target, (int, float)):
        raise ValueError("Target must be a number.")
    arr.sort()  # Ensure the array is sorted
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def quick_sort(arr):
    if not isinstance(arr, list) or not all(isinstance(x, (int, float)) for x in arr):
        raise ValueError("Input array must be a list of numbers.")
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

from collections import deque

def bfs(graph, start):
    queue = deque([start])
    visited = []
    if not isinstance(graph, dict) or not all(isinstance(k, str) and isinstance(v, list) for k, v in graph.items()):
        raise ValueError("Graph must be a dictionary with string keys and list values.")
    if not isinstance(start, str):
        raise ValueError("Start node must be a string.")
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
    return visited