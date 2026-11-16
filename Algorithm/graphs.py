# Пошук в ширину (Breadth-First Search, BFS)
# Алгоритм пошуку в ширину використовує чергу для відстеження вершин,
# які потрібно відвідати.
# Він дозволяє знаходити найкоротший шлях від стартової вершини
# до всіх інших вершин у графі.

from collections import deque


def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex)
            queue.extend(graph[vertex] - visited)

# Часова складність: O(V + E),
# де V - кількість вершин, E - кількість ребер у графі.




############################################################
# Пошук в глибину (Depth-First Search, DFS)
# Алгоритм пошуку в глибину також використовується для обходу графа.
# Він працює глибше в структуру графа, поки не досягне останньої вершини,
# а потім повертається назад, коли більше немає доступних вершин.


# def dfs(graph, start, visited=None):
#     if visited is None:
#         visited = set()
#     visited.add(start)
#     print(start)
#     for next_vertex in graph[start] - visited:
#         dfs(graph, next_vertex, visited)

# Часова складність: O(V + E),
# де V - кількість вершин, E - кількість ребер у графі.

####################################################################


# Пошук зв'язних компонентів
# Зв'язна компонента - це максимальний підграф,
# в якому між будь-якими двома вершинами існує шлях.
# Алгоритм пошуку зв'язних компонентів дозволяє
# розділити граф на окремі компоненти зв'язності.

# def connected_components(graph):
#     visited = set()
#     components = []
#     for vertex in graph:
#         if vertex not in visited:
#             component = set()
#             dfs(graph, vertex, component)
#             components.append(component)
#             visited.update(component)
#     return components

# Часова складність: O(V + E),
# де V - кількість вершин, E - кількість ребер у графі.


###############################################################

# Побудова кістякового дерева
# Кістякове дерево - це підграф зв'язного графа,
# що містить всі вершини графа та деякі ребра,
# такі що вони утворюють дерево без циклів.

# def spanning_tree(graph):
#     start_vertex = next(iter(graph))
#     visited = set()
#     tree_edges = set()
#
#     def dfs_spanning_tree(vertex):
#         visited.add(vertex)
#         for neighbor in graph[vertex]:
#             if neighbor not in visited:
#                 tree_edges.add((vertex, neighbor))
#                 dfs_spanning_tree(neighbor)
#
#     dfs_spanning_tree(start_vertex)
#     return tree_edges

# Часова складність: O(V + E),
# де V - кількість вершин, E - кількість ребер у графі.

##################################################################
# Побудова найкоротших шляхів
# Пошук найкоротших шляхів у графі дозволяє знайти
# найбільш ефективний маршрут між двома вершинами.

#...................................................
# З виділеної вершини:

# import heapq
#
#
# def dijkstra(graph, start):
#     distances = {vertex: float('infinity') for vertex in graph}
#     distances[start] = 0
#     pq = [(0, start)]
#
#     while pq:
#         current_distance, current_vertex = heapq.heappop(pq)
#
#         if current_distance > distances[current_vertex]:
#             continue
#
#         for neighbor, weight in graph[current_vertex].items():
#             distance = current_distance + weight
#             if distance < distances[neighbor]:
#                 distances[neighbor] = distance
#                 heapq.heappush(pq, (distance, neighbor))
#
#     return distances

#...................................................
# Між двома вершинами:

# def shortest_path(graph, start, end):
#     distances = {vertex: float('infinity') for vertex in graph}
#     distances[start] = 0
#     pq = [(0, start)]
#
#     while pq:
#         current_distance, current_vertex = heapq.heappop(pq)
#
#         if current_vertex == end:
#             return distances[end]
#
#         if current_distance > distances[current_vertex]:
#             continue
#
#         for neighbor, weight in graph[current_vertex].items():
#             distance = current_distance + weight
#             if distance < distances[neighbor]:
#                 distances[neighbor] = distance
#                 heapq.heappush(pq, (distance, neighbor))
#
#     return float('infinity')

#...................................................
# Часова складність для обох алгоритмів: O((V + E) * log V),
# де V - кількість вершин, E - кількість ребер у графі.



# def fibonacci(n):
#     fib = [0, 1]
#     for i in range(2, n + 1):
#         fib.append(fib[i - 1] + fib[i - 2])
#     return fib[n]
#
#
#
# def knapsack(weights, values, capacity):
#     n = len(weights)
#     dp = [[0] * (capacity + 1) for _ in range(n + 1)]
#     for i in range(1, n + 1):
#         for w in range(1, capacity + 1):
#             if weights[i - 1] <= w:
#                 dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
#             else:
#                 dp[i][w] = dp[i - 1][w]
#     return dp[n][capacity]



# def find_max(arr):
#     max_val = arr[0]
#     for num in arr:
#         if num > max_val:
#             max_val = num
#     return max_val



# def find_max(arr):
#     return max(arr)


# Приклад: сортування масиву
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr
#
# # Приклад: задача орієнтовного кольорування графа
# def graph_coloring(graph):
#     colors = {}
#     for vertex in graph:
#         neighbor_colors = set(colors.get(nei) for nei in graph[vertex] if nei in colors)
#         for color in range(len(graph)):
#             if color not in neighbor_colors:
#                 colors[vertex] = color
#                 break
#     return colors
