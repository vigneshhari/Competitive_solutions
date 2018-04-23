from GraphDS import Graph
graph = Graph(1 ,{"1": ["2", "3"], "2": ["4", "5"],
                    "3": ["5"], "4": ["6"], "5": ["6"],
                    "6": ["7"], "7": []})
#graph.addedge(1,2)
#graph.addedge(2,3)
#graph.addedge(2,5)
#graph.addedge(3,4)
print graph.BFS(1)