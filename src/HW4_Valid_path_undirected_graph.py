from collections import deque  # importing deque to use it as a fast queue (O(1) pop from left)

def valid_path(n, edges, s, t):
    # n = total number of nodes (0 to n-1)
    # edges = list of [u, v] undirected edges
    # s = start node
    # t = target node

    # if start and target are same, path exists immediately
    if s == t:  # checking if we are already at the destination
        return True  # no travel needed

    # adj will store neighbors for each node
    adj = [[] for _ in range(n)]  # create n empty lists (one list per node)

    # build adjacency list from edges
    for u, v in edges:            # take one edge at a time
        adj[u].append(v)          # add v as neighbor of u
        adj[v].append(u)          # add u as neighbor of v (because graph is undirected)

    # visited keeps track of nodes we have already processed
    visited = [False] * n         # initially mark all nodes as unvisited
    visited[s] = True             # mark start node as visited

    # queue for BFS
    q = deque([s])                # put the start node into queue

    # BFS loop: keep exploring until queue becomes empty
    while q:                      # while there are nodes to explore
        node = q.popleft()        # take the front node out of queue (FIFO)

        # check each neighbor of the current node
        for neighbor in adj[node]:            # loop over all connected nodes
            if not visited[neighbor]:         # if we haven't visited this neighbor yet
                if neighbor == t:             # if neighbor is the target node
                    return True                # we found a path

                visited[neighbor] = True      # mark neighbor as visited
                q.append(neighbor)            # add neighbor to queue to explore later

    # if BFS finishes and we never found t, there is no path
    return False



if __name__ == "__main__":  # runs only when you execute this file directly
    n = 6  # number of nodes
    edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]  # list of undirected edges
    # s = 0  # start node
    # t = 5  # target node (false case)
    s = 0  # start node
    t = 2  # target node (true case)

    print(valid_path(n, edges, s, t))  # prints True/False