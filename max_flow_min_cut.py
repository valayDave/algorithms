from typing import List
from typing import Tuple
from typing import Set
from operator import itemgetter
import sys
import numpy as np
# sys.path.append('/usr/local/opt/pygobject3/lib/python3.7/site-packages/')
# sys.path.append('/usr/local/opt/graph-tool/lib/python3.7/site-packages/')
from graph_tool.all import *
import random

# Create a graph given in the above diagram 
# $ graph[i][j] = edge_cost
# $ i = source_node_id , j = destination_node_id


class Custom_Graph:
    def __init__(self, matrix:List[List[int]]):
        self.graph = matrix
        self.org_graph =  [i[:] for i in matrix]
        self.ROW = len(matrix)

class SubSetWithDup(object):
  
    def __init__(self):
        self.result = []

    def subsetsWithDup(self, nums):
        nums = sorted(nums)
        self.dfs(nums, [])
        return self.result

    def dfs(self, nums, path):
        self.result.append(path)
        for i in range(len(nums)):
            if i == 0 or (i > 0 and nums[i-1] != nums[i]):
                self.dfs(nums[i+1:], path+[nums[i]])

# $ Finds all Combinations with elems of left_overs with  into two sets which have source and Sink Node
def extract_set_combos(source_node:int,sink_node:int,left_overs:List):
    left_overs_vals = SubSetWithDup().subsetsWithDup(left_overs)
    # del len_hash_map[0]
    # pprint.pprint(left_overs_vals)
    S = set([source_node])
    T = set([sink_node])
    left_overs_set = set(left_overs)
    combo_vals = []
    for left_over_combo  in left_overs_vals:
        new_s = set(S)
        new_t = set(T)
        new_s.update(left_over_combo)
        new_t.update(left_overs_set - set(left_over_combo))
        combo_vals.append((new_s,new_t))
        # print(new_s,new_t)

    return combo_vals


'''Returns true if there is a path from source 's' to sink 't' in 
residual graph. Also fills parent[] to store the path '''
def BFS(graph_object:Custom_Graph,s, t, parent): 

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

# $ Creates the Custom_Graph of Test Case. 
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


# $ Creates the Test case for extracting Flow
def create_test_case(source_node=0,sink_node=5):
    num_nodes = abs(sink_node-source_node)+1
    # print("Creating graph With node : ",num_nodes)
    created_graph = Custom_Graph(create_graph(num_nodes))
    parent = [-1]*(created_graph.ROW)
    if BFS(created_graph,source_node,sink_node,parent):
        return created_graph
    else:
        return create_test_case(source_node,sink_node)


# $ This is by Definition of the TESTCASE OF EVALUATION in Homework
def capacity_case1(graph_object:Custom_Graph,S:Set[int],T:Set[int]):
    return find_capacity_of_cut_sets(graph_object,S,T) - find_capacity_of_cut_sets(graph_object,T,S) 

# $ This is by Definition of the TESTCASE OF EVALUATION in Homework
def capacity_case2(graph_object:Custom_Graph,S:Set[int],T:Set[int]):
    return min([find_capacity_of_cut_sets(graph_object,S,T) ,find_capacity_of_cut_sets(graph_object,T,S)])

# $ This is by Definition of the ACTUAL ALGO
def find_flow_of_cut(graph_object:Custom_Graph,S:Set[int],T:Set[int]):
    return find_capacity_of_cut_sets(graph_object,S,T) - find_capacity_of_cut_sets(graph_object,T,S) 

# $ This is by Definition of the ACTUAL ALGO
def find_capacity_of_cut_sets(graph_object:Custom_Graph,S:Set[int],T:Set[int]):
    # c(S, T) = SUM_OF(u∈S, SUM_OF (v∈T c(u, v) ) )
    capacity = 0
    for u in S:
        for v in T:
            capacity+=graph_object.org_graph[u][v]
    return capacity

# $ Done after the Max flow is extracted. It runs a BFS to see reachable nodes from the start node and those are the part of the cut. 
def find_min_cut_from_redsidual_graph(graph_object:Custom_Graph,source_node:int,sink_node:int):
    # $ To Find cut set S,T : Do a BFS to find the nodes reachable from s in Residual Custom_Graph. They become part of S. 
    parent_arr = [-1]*(graph_object.ROW) 
    while BFS(graph_object,source_node, sink_node, parent_arr ):
        pass
    reachable_indexes= set([source_node])
    for i in range(len(parent_arr)):
        if parent_arr[i]!=-1:
            reachable_indexes.add(i)
    
    reachable_indexes_S = set(reachable_indexes)
    reachable_indexes_T = set([i for i in range(graph_object.ROW)]) - reachable_indexes_S
    return reachable_indexes_S,reachable_indexes_T

# Returns tne maximum flow from s to t in the given graph 
def find_max_flow(graph_object:Custom_Graph, source, sink): 

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
            # print(path_flow, graph_object.graph[parent[s]][s])
            path_flow = min (path_flow, graph_object.graph[parent[s]][s]) 
            s = parent[s] 
            x= (str(s)+'<--'+x)

        # print("Flow Attained From : "+x,path_flow)
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
def find_possible_cuts(graph_object:Custom_Graph,source_node:int,sink_node:int):
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
    return extract_set_combos(source_node,sink_node,left_nodes)

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

tests = list(zip(test_cases,results))
# tests = [(Custom_Graph(graph),find_max_flow(Custom_Graph(graph),0,5))]

def to_graph_tool(adj):
    g = Graph(directed=True)
    edge_weights = g.new_edge_property('double')
    g.edge_properties['weight'] = edge_weights
    nnz = np.nonzero(adj)
    nedges = len(nnz[0])
    g.add_edge_list(np.hstack([np.transpose(nnz),np.reshape(adj[nnz],(nedges,1))]),eprops=[edge_weights])
    return g

def construct_graph(graph_object:Custom_Graph):
    graph_1 = Graph(directed=True)
    vertices = []
    print(np.array(graph_object.org_graph))
    # for i in range(graph_object.ROW):
    #     for j in range(graph_object.ROW):
    #         if graph_object.org_graph[i][j] > 0:
    #             vertex_i = graph_1.vertex(i,add_missing=True)
    #             vertex_j = graph_1.vertex(j,add_missing=True)
    #             graph_1.add_edge(vertex_i,vertex_j,)
    graph_1 = to_graph_tool(np.array(graph_object.org_graph))
    # graph_draw(graph_1,vertex_text=graph_1.vertex_index, vertex_font_size=18, eprops=graph_1.ep['weight'], output="two-nodes.png")
    cap = graph_1.edge_properties["weight"]
    # state = minimize_blockmodel_dl(graph_1,state_args=dict(recs=[graph_1.ep.weight],rec_types=["real-exponential"]))
    graph_draw(graph_1,edge_text=cap, vertex_shape="double_circle",edge_color="black", vertex_text=graph_1.vertex_index,vertex_font_size=18, edge_font_size=18, edge_text_color = 'black',output="two-nodes.png")
    
    # state.draw( vertex_shape=state.get_blocks(), eprops=graph_1.ep.weight,,output="polbooks_blocks_mdl.pdf")



for test_case,op in tests:
    max_flow,min_cuts = op
    # $ Find All Possible Cuts : This is to bruteforce and check if testcases to evaluate the Questions in the Homework. 
    all_possible_cuts = find_possible_cuts(test_case,SOURCE_NODE,SINK_NODE)
    print('GRAPH ::','\n')
    print(test_case.org_graph,'\n')
    print('Max Flow : ',max_flow,'\n')
    print('Min Cut : ',min_cuts,'\n')

    # $ Find Optimal Solution / Cut of graph by following the algorithm. 
    # $ Source : https://www.cs.cmu.edu/~ckingsf/bioinfo-lectures/netflow.pdf
    reachable_indexes_S,reachable_indexes_T =find_min_cut_from_redsidual_graph(test_case,SOURCE_NODE,SINK_NODE)
    flow_by_definition = find_flow_of_cut(test_case,reachable_indexes_S,reachable_indexes_T)
    capacity_of_cut = find_capacity_of_cut_sets(test_case,reachable_indexes_S,reachable_indexes_T)
    capacity_of_cut_case1 = capacity_case1(test_case,reachable_indexes_S,reachable_indexes_T)
    capacity_of_cut_case2 = capacity_case2(test_case,reachable_indexes_S,reachable_indexes_T) 
    print('Extracting CUT From BFS Of Residual Graph.','\n')
    print('cuts :',reachable_indexes_S,reachable_indexes_T)
    print('flow_by_definition',flow_by_definition)
    print('capacity_of_cut',capacity_of_cut)
    print('capacity_of_cut_case1',capacity_of_cut_case1)
    print('capacity_of_cut_case2',capacity_of_cut_case2, '\n')
    
    cut_data = []
    for cut in all_possible_cuts:
        S,T = cut
        flow_by_definition = find_flow_of_cut(test_case,S,T)
        capacity_of_cut = find_capacity_of_cut_sets(test_case,S,T)
        capacity_of_cut_case1 = capacity_case1(test_case,S,T)
        capacity_of_cut_case2 = capacity_case2(test_case,S,T) 
        cut_data.append((cut,flow_by_definition,capacity_of_cut_case1,capacity_of_cut_case2,capacity_of_cut))
        # if flow_by_definition <= max_flow and flow_by_definition > 0:
        #     print("Testing Cut : ",cut, capacity_of_cut == max_flow)
        #     print('max_flow',max_flow)
        #     print("flow_by_definition ",flow_by_definition)
        #     print('capacity_of_cut',capacity_of_cut)
        #     print('capacity_of_cut_case1',capacity_of_cut_case1)
        #     print('capacity_of_cut_case2',capacity_of_cut_case2,'\n')
    # $ Find Min Capacity From all cuts according to capacity definition in question and print thier Cut values. 
    capacity_of_cut_case1_max_data = min(cut_data,key=itemgetter(2))
    capacity_of_cut_case2_max_data = min(cut_data,key=itemgetter(3))
    # print('max_flow',max_flow,'\n')
    print("capacity_of_cut_case1_max_data",'\n')
    print('cuts',capacity_of_cut_case1_max_data[0])
    print('flow_by_definition',capacity_of_cut_case1_max_data[1])
    print('capacity_case1',capacity_of_cut_case1_max_data[2])
    print('capacity_case1',capacity_of_cut_case1_max_data[2])
    print('capacity_case2',capacity_of_cut_case1_max_data[3])
    print('capacity_of_cut',capacity_of_cut_case1_max_data[4],'\n')
    
    print("capacity_of_cut_case2_max_data",'\n')
    print('cuts',capacity_of_cut_case2_max_data[0])
    print('flow_by_definition',capacity_of_cut_case2_max_data[1])
    print('capacity_case1',capacity_of_cut_case2_max_data[2])
    print('capacity_case2',capacity_of_cut_case2_max_data[3])
    print('capacity_of_cut',capacity_of_cut_case2_max_data[4],'\n')

    capacity_of_cut_min_data = min(cut_data,key=itemgetter(4))
    print("Capacity Cut From Min Capacity Of All Possible Cuts. ",'\n')
    print('cuts',capacity_of_cut_min_data[0])
    print('flow_by_definition',capacity_of_cut_min_data[1])
    print('capacity_case1',capacity_of_cut_min_data[2])
    print('capacity_case2',capacity_of_cut_min_data[3])
    print('capacity_of_cut',capacity_of_cut_min_data[4],'\n\n')

    construct_graph(test_case)
    
    # for cut in cut_data:
    #     print(*cut)
        