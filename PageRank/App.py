from email.generator import Generator
import tkinter as tk
from tkinter import INSERT, filedialog as fd
import pathlib

from Graph import Graph, GraphTypes
from Generator import Generator
from PageRank import PageRank

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.graph = Graph()

        self.title('Graphs - Project 1')
        self.geometry('1360x720')

        self.create_widgets()

    def load_from_file(self) -> None:
        # Allowed file types
        file_types = (
            ("Adjacency List", "*.adjl"),
            ("Adjacency Matrix", "*.adjm"),
            ("Incidence Matrix", "*.incm")
        )

        file = fd.askopenfile(
            title="Open a file",
            initialdir=".",
            filetypes=file_types
        )

        # File opened 
        if file:
            self.reset_buttons()

            # File extension without dot character
            extension = pathlib.Path(file.name).suffix[1:]

            # Loading file to corresponding structure
            if extension == 'adjl':
                self.graph.content = Graph.load_adjacency_list(file.name)
                self.graph.type = GraphTypes.AdjacencyList
                self.graph_text_output.insert(INSERT, Graph.adjacency_list_to_str(self.graph.content))
            else:
                print("Unknown Error")
                exit(-1)


    def generate_graph(self):
        self.graph.type = GraphTypes.AdjacencyList
        self.graph.content = Generator.generate(int(self.n_input.get()), float(self.lp_input.get()))
        self.reset_buttons()
        self.graph_text_output.insert(INSERT, Graph.adjacency_list_to_str(self.graph.content))


    def visualize_graph(self):
        self.graph.visualize(self.graph_image_output)

    def reset_buttons(self) -> None:
        self.graph_text_output.delete('1.0', 'end')
    
    def reset_PageRankOutput(self) -> None:
        self.power_iteration_text_output.delete('1.0', 'end')
        self.monte_carlo_text_output.delete('1.0', 'end')

    def calculate_PageRank(self) -> None:
        self.reset_PageRankOutput()
        self.monte_carlo_text_output.insert(INSERT, PageRank.monteCarlo(self.graph.content))
        self.power_iteration_text_output.insert(INSERT, PageRank.power_iteration(self.graph.content))








    def create_widgets(self) -> None:
        self.load_button = tk.Button(self, text='Load from file', command=self.load_from_file)
        self.load_button.grid(column=0, row=0, padx=10, pady=10)

        self.n_label = tk.Label(self, text='Verticles: ')
        self.n_label.grid(column=0, row=1)

        self.n_input = tk.Entry(self)
        self.n_input.grid(column=0, row=2)

        self.lp_label = tk.Label(self, text='Edges: ')
        self.lp_label.grid(column=0, row=3)

        self.lp_input = tk.Entry(self)
        self.lp_input.grid(column=0, row=4)

        self.generate_gnl_button = tk.Button(self, text='Generate graph(n, l)', command=self.generate_graph)
        self.generate_gnl_button.grid(column=0, row=5, padx=10, pady=10)

        self.visualize_button = tk.Button(self, text='Visualize Graph', command=self.visualize_graph)
        self.visualize_button.grid(column=0, row=6, padx=10, pady=10)

        self.visualize_button = tk.Button(self, text='Calculate', command=self.calculate_PageRank)
        self.visualize_button.grid(column=0, row=7, padx=10, pady=10)

        self.lp_label = tk.Label(self, text='Input: ')
        self.lp_label.grid(column=1, row=0)
        self.graph_text_output = tk.Text(self, width=40, height=14)
        self.graph_text_output.grid(column=1, row=1, rowspan=3, padx=10, pady=10)


        self.monte_carlo_label = tk.Label(self, text='MonteCarlo: ')
        self.monte_carlo_label.grid(column=0, row=8)
        self.monte_carlo_text_output = tk.Text(self, width=40, height=14)
        self.monte_carlo_text_output.grid(column=0, row=9, rowspan=12, padx=10, pady=10)

        self.power_iteration_label = tk.Label(self, text='Power iteration: ')
        self.power_iteration_label.grid(column=1, row=8)
        self.power_iteration_text_output = tk.Text(self, width=40, height=14)
        self.power_iteration_text_output.grid(column=1, row=9, rowspan=12, padx=10, pady=10)

        self.graph_image_output = tk.Canvas(self, bg='white', width=600, height=600)
        self.graph_image_output.grid(column=2, row=0, rowspan=14, padx=10, pady=10)
