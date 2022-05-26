import math
import tkinter as tk
from collections import defaultdict
from enum import Enum

class GraphTypes(Enum):
    AdjacencyList = 1,
    AdjacencyMatrix = 2,
    IncidenceMatrix = 3

class Graph:
    def __init__(self):
        self.content = None
        self.type = None

    def visualize(self, canvas: tk.Canvas) -> None:
        canvas.delete('all')


        graph_copy = self.content.copy()



        vertices_number = len(graph_copy)
        center_x = canvas.winfo_width() / 2
        center_y = canvas.winfo_height() / 2 
        radius = min(center_x, center_y) / 1.25
        angle = 2 * math.pi / vertices_number

        positions: list = []

        canvas.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius, outline='red', width=2, dash=(100, 50))

        arrow_len = min(center_x, center_y) / 20
        arrow_delta = math.pi * 20. / 180

        for i in range(0, vertices_number):
            current_angle = i * angle
            x = center_x + radius * math.sin(current_angle)
            y = center_y - radius * math.cos(current_angle)
            
            for connected_edge in graph_copy[i + 1]:
                connected_edge = connected_edge - 1
                conneted_angle = connected_edge * angle
                connected_x = center_x + radius * math.sin(conneted_angle)
                connected_y = center_y - radius * math.cos(conneted_angle)
                
                segment_len = math.sqrt((connected_x-x)*(connected_x-x) + (connected_y-y) * (connected_y-y)) - radius * 0.1



                arrow_angle = math.atan2(connected_x-x, connected_y-y)

                arrx1 = x+ segment_len * math.sin(arrow_angle) - arrow_len * math.sin(arrow_angle+arrow_delta)
                arry1 = y+segment_len * math.cos(arrow_angle) - arrow_len * math.cos(arrow_angle+arrow_delta)
                arrx2 = x+segment_len * math.sin(arrow_angle) - arrow_len * math.sin(arrow_angle-arrow_delta)
                arry2 = y+segment_len * math.cos(arrow_angle) - arrow_len * math.cos(arrow_angle-arrow_delta)
                canvas.create_line(arrx1, arry1, x+ segment_len * math.sin(arrow_angle),y+segment_len * math.cos(arrow_angle), width=3)
                canvas.create_line(arrx2, arry2, x+ segment_len * math.sin(arrow_angle),y+segment_len * math.cos(arrow_angle), width=3)
                canvas.create_line(x, y, connected_x, connected_y, width=3)
            
            positions.append((x, y))
            
        for i in range(0, vertices_number):
            x, y = positions[i]
            scale = 0.1
            pos = (x - radius * scale, y - radius * scale, x + radius * scale, y + radius * scale)
            canvas.create_oval(pos[0], pos[1], pos[2], pos[3], outline='#343aeb', fill='#6b7cc9', width=2.5)
            canvas.create_text(x, y, text=str(i + 1), font=('Arial',int(radius * scale/2),'bold'))

    @staticmethod
    def load_adjacency_list(path:str) -> dict:
        adjacency_list = defaultdict(list)

        with open(path) as file:
            lines = file.readlines()
            counter = 1

            for line in lines:
                line = line.strip()
                line = line.split(' ')

                for element in line:
                    if not element.endswith('.'):
                        adjacency_list[counter].append(int(element))

                counter += 1

        return adjacency_list

    @staticmethod
    def adjacency_list_to_str(adj_list: dict) -> str:
        result: str = ''

        for key in adj_list:
            result += str(key) + '.'
            for element in adj_list[key]:
                result += ' ' + str(element)

            result += '\n'

        return result