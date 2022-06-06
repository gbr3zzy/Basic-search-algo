from collections import defaultdict



# Tree structure

class Node:

    def __init__(self):

        # default dictionary to store graph

        # key : Node , values : NeighbouringNodes

        self.graph = defaultdict(list)



    # since graph is bidirectional, add as neighbour both ways (both sources)

    def add_edge(self, u: int, v: int):

        self.graph[u].append(v)

        self.graph[v].append(u)



    def bfs(self, source: int):



        bfs_traverse = []



        # keep track of nodes traversed already

        is_visited = [False] * len(self.graph)

        # Queue used for keeping track of next node to be travelled - start with Source

        queue = [source]



        # mark source as visited (as its already added to queue_

        is_visited[source] = True



        while len(queue) > 0:



            # pop (first) element of the queue

            curr_node = queue.pop(0)

            bfs_traverse.append(curr_node)



            # add the neighbouring nodes that were still not visited

            for neighbour_node in self.graph[curr_node]:

                if not is_visited[neighbour_node]:

                    queue.append(neighbour_node)

                    # make visited True as they join queue

                    is_visited[neighbour_node] = True



        return bfs_traverse





def run_bfs(node: Node, source: int):

    return node.bfs(source)



# main

if __name__ == "__main__":





    node = Node()

    node.add_edge(0, 1)

    node.add_edge(0, 2)

    node.add_edge(1, 3)

    node.add_edge(1, 4)

    node.add_edge(2, 4)

    node.add_edge(3, 4)

    node.add_edge(3, 5)

    node.add_edge(4, 5)



    bfs_traverse = run_bfs(node, 0)



    print("Search Algo")

    print(' '.join(str(ele) for ele in bfs_traverse))
