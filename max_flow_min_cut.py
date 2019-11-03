from typing import List
from typing import Tuple
from typing import Set

import random

# Create a graph given in the above diagram 
# $ graph[i][j] = edge_cost
# $ i = source_node_id , j = destination_node_id


class Graph:
    def __init__(self, matrix:List[List[int]]):
        self.graph = matrix
        self.org_graph =  [i[:] for i in matrix]
        self.ROW = len(matrix)


'''Returns true if there is a path from source 's' to sink 't' in 
residual graph. Also fills parent[] to store the path '''
def BFS(graph_object:Graph,s, t, parent): 

    # Mark all the vertices as not visited 
    visited =[False]*(graph_object.ROW) 
        
    # Create a queue for BFS 
    queue=[] 
        
    # Mark the source node as visited and enqueue it 
    queue.append(s) 
    visited[s] = True
        
    # Standard BFS Loop 
    while queue: 

        #Dequeue a vertex from queue and print it 
        u = queue.pop(0) 
        
        # Get all adjacent vertices of the dequeued vertex u 
        # If a adjacent has not been visited, then mark it 
        # visited and enqueue it 
        for ind, val in enumerate(graph_object.graph[u]): 
            if visited[ind] == False and val > 0 : 
                queue.append(ind) 
                visited[ind] = True
                parent[ind] = u 

    # If we reached sink in BFS starting from source, then return 
    # true, else false 
    return True if visited[t] else False
            

def create_graph(num_nodes=6,max_edge_value=20):
    graph = []
    for i in range(num_nodes):
        row = []
        if i == num_nodes-1:
            row =  [0 for j in range(num_nodes)]
        else:
            for j in range(num_nodes):
                if i == j or (i == 0 and j == num_nodes -1):
                    row.append(0)
                elif random.randint(0,1) == 1:
                    row.append(random.randint(1,max_edge_value))
                else:
                    row.append(0)
                
        graph.append(row)
    return graph


def create_test_case(source_node=0,sink_node=5):
    num_nodes = abs(sink_node-source_node)+1
    print("Creating graph With node : ",num_nodes)
    created_graph = Graph(create_graph(num_nodes))
    parent = [-1]*(created_graph.ROW)
    if BFS(created_graph,source_node,sink_node,parent):
        return created_graph
    else:
        return create_test_case(source_node,sink_node)

def capacity_case1(graph_object:Graph,S:Set[int],T:Set[int]):
    return find_capacity_of_cut_sets(graph_object,S,T) - find_capacity_of_cut_sets(graph_object,T,S) 

def capacity_case2(graph_object:Graph,S:Set[int],T:Set[int]):
    return min([find_capacity_of_cut_sets(graph_object,S,T) ,find_capacity_of_cut_sets(graph_object,T,S)])

def find_flow_of_cut(graph_object:Graph,S:Set[int],T:Set[int]):
    return find_capacity_of_cut_sets(graph_object,S,T) - find_capacity_of_cut_sets(graph_object,T,S) 

def find_capacity_of_cut_sets(graph_object:Graph,S:Set[int],T:Set[int]):
    # c(S, T) = SUM_OF(u∈S, SUM_OF (v∈T c(u, v) ) )
    capacity = 0
    for u in S:
        for v in T:
            capacity+=graph_object.org_graph[u][v]
    return capacity

def find_cut_from_edges(graph_object:Graph,edges:List[Tuple[int,int]]):
    S = set()
    T = set()
    V = set([i for i in range(graph_object.ROW)])
    for source_node,goal_node in edges:
        if source_node not in T:
            S.add(source_node)
        else:
            S.update(V - T)
            break
        if goal_node not in S:
            T.add(goal_node)
        else:
            S.update(V - T)
            break
    X = set(S)
    if X.update(T) == V:
        return S,T
    else:
        S.update(V - T)
        return S,T

def find_cut():
    # http://www.cs.toronto.edu/~lalla/373s16/notes/MFMC.pdf
    '''
    Let (G, s, t, c) be a flow network,
        
        an s-t cut in G is a partition of V into two sets S and T

            such that:
            1. S ∪ T = V
            2. S ∩ T = ∅
            3. s ∈ S and t ∈ T

        c is the capacity function c(S,T) 
    '''
    pass
    
# Returns tne maximum flow from s to t in the given graph 
def find_max_flow(graph_object:Graph, source, sink): 

    # This array is filled by BFS and to store path 
    parent = [-1]*(graph_object.ROW) 
    # It will hold the parent_indexs of each of the nodes. The actual index of this array reps node_index so it maps parent[node_index] = parent_index

    max_flow = 0 # There is no flow initially 
    # print("Starting With Parent",parent)
    # Augment the flow while there is path from source to sink 
    while BFS(graph_object,source, sink, parent) : 
        # print(parent)
        # Find minimum residual capacity of the edges along the 
        # path filled by BFS. Or we can say find the maximum flow 
        # through the path found. 
        path_flow = float("Inf") 
        s = sink 
        x = str(s)


        while(s !=  source):
            print(path_flow, graph_object.graph[parent[s]][s])
            path_flow = min (path_flow, graph_object.graph[parent[s]][s]) 
            s = parent[s] 
            x= (str(s)+'<--'+x)

        print("Flow Attained From : "+x,path_flow)
        # Add path flow to overall flow 
        max_flow +=  path_flow 

        # update residual capacities of the edges and reverse edges 
        # along the path 
        v = sink 
        while(v !=  source): 
            u = parent[v] 
            graph_object.graph[u][v] -= path_flow 
            graph_object.graph[v][u] += path_flow 
            v = parent[v] 
        # print(graph_object.graph)
        
    # $ TO Find Min Cut find All edges which are from a reachable vertex to non-reachable vertex are minimum cut edges. 
    # $ Print all such edges.
    # print(graph_object.org_graph)
    # print(graph_object.graph)
    min_cuts = []
    min_cut_total= 0
    for i in range(graph_object.ROW): 
            for j in range(graph_object.ROW): 
                if graph_object.graph[i][j] == 0 and graph_object.org_graph[i][j] > 0: 
                    min_cuts.append((i,j))
                    min_cut_total+=graph_object.org_graph[i][j]

    return max_flow,min_cuts


# $ Creates all posssible cuts from the given graph. 
def find_possible_cuts(graph_object:Graph,source_node:int,sink_node:int):
    '''
    an s-t cut in G is a partition of V into two sets S and T
    such that:
    1. S ∪ T = V
    2. S ∩ T = ∅
    3. s ∈ S and t ∈ T
    '''
    V = set([i for i in range(graph_object.ROW)])
    S = set([source_node])
    T = set([sink_node])
    left_nodes = V - S
    left_nodes = left_nodes - T
    left_nodes = list(left_nodes)
    possibles_cuts = [
        # S , T 
    ]
    created_map = {

    }
    for i in range(len(left_nodes)):
        val_1 = set([left_nodes[i]])    
        iterating_nodes = list(set(left_nodes) - val_1)
        continuous_index = i
        for j in range(len(iterating_nodes)+1):
            new_s = set(S)
            new_val_1 = set(val_1)
            new_val_1.update(set(iterating_nodes[continuous_index:j]))
            new_s.update(new_val_1)
            # print(new_s) 
            new_val1_str = ''.join([str(k) for k in list(new_s)])
            if new_val1_str in created_map:
                continuous_index = j
                continue
            created_map[new_val1_str] = 1
            val_2 = set(iterating_nodes) - new_val_1
            new_t = set(T)
            new_t.update(val_2)
            possibles_cuts.append((new_s,new_t))
        
    return possibles_cuts

# $ ASSERTION “Maximum flow from a source node s to a destination node t is equal to capacity of the maximum cut”

SOURCE_NODE = 0

SINK_NODE = 5

graph = [[0, 16, 13, 0, 0, 0], 
        [0, 0, 10, 12, 0, 0], 
        [0, 4, 0, 0, 14, 0], 
        [0, 0, 9, 0, 0, 20], 
        [0, 0, 0, 7, 0, 4], 
        [0, 0, 0, 0, 0, 0]] 


test_cases = [(create_test_case(SOURCE_NODE,SINK_NODE)) for i in range(1)]
results = [find_max_flow(test_case,SOURCE_NODE,SINK_NODE) for test_case in test_cases]



# tests = list(zip(test_cases,results))
tests = [(Graph(graph),find_max_flow(Graph(graph),0,5))]

for test_case,op in tests:
    print('GRAPH :: \n',test_case.org_graph)
    max_flow,min_cuts = op
    all_possible_cuts = find_possible_cuts(test_case,SOURCE_NODE,SINK_NODE)
    print('Max Flow : ',max_flow,'\n')
    print('Min Cut : ',min_cuts,'\n')
    for cut in all_possible_cuts:
        S,T = cut
        flow_by_definition = find_flow_of_cut(test_case,S,T)
        capacity_of_cut = find_capacity_of_cut_sets(test_case,S,T)
        capacity_of_cut_case1 = capacity_case1(test_case,S,T)
        capacity_of_cut_case2 = capacity_case2(test_case,S,T) 
        print("Testing Cut : ",cut, flow_by_definition == max_flow)
        print('max_flow',max_flow)
        print("flow_by_definition ",flow_by_definition)
        print('capacity_of_cut',capacity_of_cut)
        print('capacity_of_cut_case1',capacity_of_cut_case1)
        print('capacity_of_cut_case2',capacity_of_cut_case2)

    