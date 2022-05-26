from tracemalloc import start
import numpy as np
from collections import defaultdict

class Converter:
    @staticmethod
    def adj_list_to_adj_matrix(adj_list: dict) -> np.ndarray:
        size = len(adj_list)
        adj_matrix = np.zeros((size, size), int)

        for key in adj_list:
            row = adj_list[key]
            for element in row:
                adj_matrix[key-1][element-1] = 1
                adj_matrix[element-1][key-1] = 1

        return adj_matrix

    @staticmethod
    def adj_list_to_inc_matrix(adj_list: dict) -> np.ndarray:
        adj_matrix: np.ndarray = Converter.adj_list_to_adj_matrix(adj_list)
        return Converter.adj_matrix_to_inc_matrix(adj_matrix)

    @staticmethod
    def adj_matrix_to_adj_list(adj_matrix: np.ndarray) -> dict:
        adj_list = defaultdict(list)
        x, y = adj_matrix.shape
        
        for i in range(0, x):
            for j in range(0, y):
                if adj_matrix[i][j] == 1:
                    adj_list[i+1].append(j+1)

        return adj_list

    @staticmethod
    def adj_matrix_to_inc_matrix(adj_matrix: np.ndarray) -> np.ndarray:
        x, y = adj_matrix.shape
        edges = 0

        for i in range(0, x):
            for j in range (0, y):
                if adj_matrix[i][j] == 1:
                    edges += 1

        edges = int(edges / 2)

        inc_matrix = np.zeros((x, edges), int)
        current_edge = 0

        for i in range(0, x):
            for j in range(i+1, y):
                if(adj_matrix[i][j] == 1):
                    inc_matrix[i][current_edge] = 1
                    inc_matrix[j][current_edge] = 1
                    current_edge = current_edge + 1  
                
        return inc_matrix

    @staticmethod
    def inc_matrix_to_adj_list(inc_matrix: np.ndarray) -> dict:
        adj_matrix: np.ndarray = Converter.inc_matrix_to_adj_matrix(inc_matrix)
        return Converter.adj_matrix_to_adj_list(adj_matrix)

    @staticmethod
    def inc_matrix_to_adj_matrix(inc_matrix: np.ndarray) -> np.ndarray:
        vertices_number, edges_number = inc_matrix.shape

        adj_matrix: np.ndarray = np.zeros((vertices_number, vertices_number), int)

        for i in range(0, edges_number):
            start_edge = None
            end_edge = None

            for j in range(0, vertices_number):
                if inc_matrix[j][i] == 1:
                    if start_edge is None:
                        start_edge = j
                    else:
                        end_edge = j
            
            adj_matrix[start_edge][end_edge] = 1
            adj_matrix[end_edge][start_edge] = 1

        return adj_matrix