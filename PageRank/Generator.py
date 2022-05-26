import random
from tracemalloc import start
from collections import defaultdict

class Generator:
    @staticmethod
    def generate(n: int, l: int) -> dict:

        vertices_number = n
        edges_number = l
        generated_edges = 0
        adjacency_list = defaultdict(list)
        if edges_number < vertices_number-1:
            edges_number = vertices_number-1
        elif edges_number > int(vertices_number * (vertices_number - 1)):
            edges_number = int(vertices_number * (vertices_number - 1))

        for i in range(1, n+1):
            r = i
            while r == i:
                r = random.randint(1, int(n) )
            adjacency_list[i].append(r)
            generated_edges = generated_edges+1

        while generated_edges < edges_number:
            r = random.randint(1, n)
            a = random.randint(1, n)
            if len(adjacency_list[r]) == n-1:
                continue
            while a in adjacency_list[r] or a == r:
                a = random.randint(1, n)
            adjacency_list[r].append(a)
            generated_edges = generated_edges+1

        return adjacency_list