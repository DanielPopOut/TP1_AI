from heapqueue.binary_heap import BinaryHeap
import queue as Q
import copy

from Graph import Graph
import Kruskal
from Solution import Solution

SOURCE = 0

class Node(object):
    def __init__(self, v, sol, heuristic_cost=0):
        self.v = v
        self.solution = copy.deepcopy(sol)
        self.heuristic_cost = heuristic_cost

    def explore_node(self, heap):
        for nVisited in self.solution.not_visited:
            if nVisited == 0 and len(self.solution.not_visited) > 1:
                continue
            solution = Solution(self.solution)
            solution.add_edge(self.v, nVisited)
            node = Node(nVisited, solution)
            heap.put(node)
    def __lt__ (self, N):
        return isN2betterThanN1(N, self)

def main():
    g = Graph("N10.data")
    import Kruskal #prof
    Kruskal.kruskal = Kruskal.Kruskal(g)
    heap = Q.PriorityQueue()
    s = Solution(g)
    n = Node(SOURCE, s)
    

    while len(n.solution.not_visited) != 0 :
        n.explore_node(heap)
        n = heap.get()
    n.solution.print()        
		
			
		

def isN2betterThanN1(N1, N2):
    fN1 = N1.heuristic_cost + N1.solution.cost
    fN2 = N2.heuristic_cost + N2.solution.cost
    if fN2 < fN1:
        return True
    return False

if __name__ == '__main__':
    main()
