import copy
from Graph import Graph

SOURCE = 0
class Solution(object):
    def __init__(self, s):
        if isinstance(s, Graph):
            self.g = s
            self.cost = 0
            self.visited = []
            self.not_visited = []
            for i in range(self.g.N):
                self.not_visited.append(i)
        elif isinstance(s, Solution):
            self.g = s.g 
            self.cost = s.cost
            self.visited = copy.deepcopy(s.visited)
            self.not_visited = copy.deepcopy(s.not_visited)
        else:
            raise ValueError('you should give a graph or a solution')

    def add_edge(self, v, u):
        self.visited.append(u)
        self.cost = self.cost + self.g.costs[u, v]
        self.not_visited.remove(u)
	#self.visited.remove(self.visited.index(v))
	
    def print(self):
        print(SOURCE)
        for vertex in self.visited:
            print(vertex)
        print("COST = " + str(self.cost))
		
