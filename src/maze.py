import networkx as nx
from matplotlib import pyplot as plt
import random
from copy import deepcopy

class Maze:
    """
    Maze object, generated using Depth First Search (DFS).
    """
    def __init__(self, h=20, w=40, viz=True):
        self.G = nx.grid_2d_graph(h,w)
        self.viz = viz
        self.generate_maze()
        
    def visualize(self):
        """
        Visualization function to display generated maze, using 
        networkx's inbuilt draw() function with matplotlib's pyplot. 
        
        Saves the figure as a png in the local directory.
        """
        plt.figure(figsize=(40,20))
        pos = {(x,y):(y,-x) for x,y in self.G.nodes()}
        nx.draw(self.G, pos=pos, 
                with_labels=False, 
                node_size=0,
                width=self.weights)
        plt.savefig('mz')

    def generate_maze(self):
        """
        Initializes variables and calls self.dfs() to generate the set of weights
        necessary for the creation of the maze. 
        """
        self.marked = {k:False for k in self.G.nodes()}
        self.edges = list(self.G.edges())
        self.weights = [0]*len(self.edges) 
        self.dfs((0,0))
        if self.viz:
            self.visualize()
    
    def dfs(self, v, p=None):
        """
        Randomized recursive Depth First Search (DFS) implementation. 
        
        Inputs: 
        v - current node
        p - previous node
        
        Result is the population of self.weights, to be visualized as a maze. 
        """
        
        if p:
            try:
                w_ind = self.edges.index((p,v))
                self.weights[w_ind] = 1 # Darken an edge to visit. 

            except ValueError:
                w_ind = self.edges.index((v,p))
                self.weights[w_ind] = 1 # Darken an edge to visit.  

        self.marked[v] = True

        v_neigh = list(self.G.neighbors(v))
        random.shuffle(v_neigh)

        for w in v_neigh:
            if not self.marked[w]:
                self.dfs(w,p=v)
        
def main():
    Maze()

if __name__ == '__main__':
    main()
    