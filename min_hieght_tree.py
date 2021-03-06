'''
For an undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of undirected edges (each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Example 1 :

Input: n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3 

Output: [1]
Example 2 :

Input: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5 

Output: [3, 4]
Note:

According to the definition of tree on Wikipedia: “a tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.”
The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.
'''
from typing import List,Dict

def dfs(root_node:int, node_graph:Dict):
    stack = list([root_node])
    curr_root = root_node
    visited = [root_node]
    max_height = 0
    curr_height = 0
    while len(stack) > 0:
        curr_node = stack.pop()
        node_graph[curr_node] = [i for i in node_graph[curr_node] if i not in visited]
        print("Visited :",curr_node,root_node,curr_height,visited,node_graph[curr_node],stack)
        if len(node_graph[curr_node]) > 0:
            stack.append(curr_node)
            stack.append(node_graph[curr_node].pop())
            curr_height+=1
        else:
            if curr_height+1 > max_height:
                max_height = curr_height+1
            curr_height-=1

        if curr_node not in visited:
            visited.append(curr_node)
    return max_height             
        
    

def min_tree(n: int, edges: List[List[int]])->List[int]:
    if n == 1:
        return [0]
    if n == 2 and len(edges) == 1:
        return [0,1]
    
    node_graph = {}
    for i in range(n):
        node_graph[i] = []

    for edge in edges:
        if len(edge) > 1:
            node_graph[edge[0]].append(edge[1])
            node_graph[edge[1]].append(edge[0])

    # print(node_graph)
    no_edge_nodes = [key for key in node_graph if len(node_graph[key]) == 0]
    if len(no_edge_nodes) > 0:
        return no_edge_nodes
    
    # # $ Find if there are any cycles to give graph. 
    # node_connections = [sorted(node_graph[key]+[key]) for key in node_graph]
    # node_connections.sort(key=len)
    # if len(node_connections) > 2: # $ Check for cycles when there are more than 2 nodes. 
    #     for i,connection in enumerate(node_connections):
    #         for j in range(i+1,len(node_connections)):
    #             if len(connection) != len(node_connections[j]):
    #                 break
    #             if node_connections[j] == connection: # $ This Means that it is has a cycle. 
    #                 return []
    
    # print("here")
    # if len(node_connections[0]) == 0:
    node_heights = {}
    # A node that w 

    for root_node in node_graph:
        if len(node_graph[root_node]) == 1:
            continue
        max_height = dfs(root_node,dict(node_graph))
        node_heights[root_node] = max_height
    
    # print(node_graph)
    print(node_heights)
    min_nodes=[]
    for root_node in node_heights:
        if len(min_nodes) == 0:
            min_nodes.append(root_node)
            continue
        if node_heights[root_node] < node_heights[min_nodes[0]]:
            min_nodes = [root_node]
        elif  node_heights[root_node] == node_heights[min_nodes[0]]:
            min_nodes += [root_node]
    # print('min_nodes', min_nodes)
    return min_nodes


x=min_tree(4,[[1, 0], [1, 2], [1, 3]])
x=min_tree(6,[[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]])
x=min_tree(2,[[0,1]])
# x=min_tree(315,[[0,1],[0,2],[2,3],[1,4],[2,5],[0,6],[2,7],[7,8],[2,9],[7,10],[6,11],[5,12],[6,13],[8,14],[3,15],[5,16],[15,17],[13,18],[16,19],[4,20],[1,21],[0,22],[18,23],[13,24],[8,25],[10,26],[17,27],[17,28],[26,29],[27,30],[13,31],[13,32],[21,33],[14,34],[12,35],[21,36],[28,37],[28,38],[16,39],[35,40],[23,41],[40,42],[39,43],[20,44],[1,45],[36,46],[43,47],[36,48],[47,49],[49,50],[0,51],[24,52],[20,53],[46,54],[23,55],[35,56],[43,57],[38,58],[38,59],[57,60],[39,61],[37,62],[52,63],[11,64],[54,65],[30,66],[24,67],[52,68],[58,69],[5,70],[17,71],[63,72],[40,73],[26,74],[20,75],[30,76],[45,77],[52,78],[46,79],[67,80],[3,81],[33,82],[12,83],[1,84],[82,85],[28,86],[65,87],[62,88],[66,89],[84,90],[86,91],[31,92],[80,93],[79,94],[48,95],[64,96],[7,97],[90,98],[30,99],[12,100],[33,101],[82,102],[28,103],[82,104],[88,105],[0,106],[42,107],[48,108],[50,109],[57,110],[2,111],[97,112],[16,113],[52,114],[60,115],[6,116],[26,117],[61,118],[32,119],[50,120],[65,121],[3,122],[113,123],[46,124],[7,125],[119,126],[82,127],[89,128],[101,129],[27,130],[104,131],[8,132],[19,133],[127,134],[38,135],[16,136],[16,137],[96,138],[8,139],[121,140],[110,141],[101,142],[51,143],[4,144],[131,145],[38,146],[44,147],[80,148],[95,149],[43,150],[113,151],[123,152],[50,153],[141,154],[88,155],[83,156],[42,157],[10,158],[102,159],[142,160],[14,161],[92,162],[13,163],[41,164],[73,165],[140,166],[90,167],[30,168],[68,169],[4,170],[100,171],[98,172],[0,173],[14,174],[15,175],[78,176],[91,177],[23,178],[23,179],[67,180],[54,181],[64,182],[172,183],[173,184],[159,185],[26,186],[93,187],[105,188],[60,189],[144,190],[133,191],[170,192],[163,193],[156,194],[116,195],[110,196],[103,197],[81,198],[79,199],[70,200],[133,201],[20,202],[12,203],[135,204],[201,205],[148,206],[132,207],[37,208],[19,209],[96,210],[151,211],[166,212],[142,213],[175,214],[134,215],[140,216],[176,217],[83,218],[120,219],[205,220],[157,221],[64,222],[93,223],[164,224],[82,225],[74,226],[215,227],[40,228],[109,229],[53,230],[68,231],[133,232],[49,233],[125,234],[230,235],[11,236],[134,237],[90,238],[107,239],[139,240],[139,241],[226,242],[77,243],[53,244],[79,245],[137,246],[200,247],[148,248],[212,249],[197,250],[230,251],[214,252],[190,253],[117,254],[22,255],[156,256],[143,257],[42,258],[48,259],[178,260],[109,261],[9,262],[65,263],[167,264],[246,265],[112,266],[11,267],[207,268],[34,269],[128,270],[186,271],[102,272],[88,273],[15,274],[169,275],[198,276],[260,277],[24,278],[198,279],[33,280],[121,281],[105,282],[93,283],[229,284],[24,285],[267,286],[21,287],[258,288],[142,289],[212,290],[84,291],[2,292],[50,293],[253,294],[114,295],[80,296],[36,297],[128,298],[2,299],[166,300],[279,301],[116,302],[144,303],[72,304],[256,305],[236,306],[29,307],[78,308],[258,309],[8,310],[15,311],[272,312],[14,313],[93,314]])
# x=min_tree(357,[[0,1],[0,2],[1,3],[3,4],[0,5],[4,6],[3,7],[5,8],[4,9],[0,10],[3,11],[6,12],[8,13],[4,14],[12,15],[4,16],[5,17],[9,18],[15,19],[2,20],[5,21],[17,22],[16,23],[22,24],[13,25],[8,26],[14,27],[1,28],[0,29],[24,30],[16,31],[18,32],[30,33],[30,34],[24,35],[16,36],[22,37],[26,38],[23,39],[1,40],[7,41],[15,42],[26,43],[42,44],[10,45],[29,46],[14,47],[31,48],[22,49],[28,50],[44,51],[23,52],[49,53],[14,54],[2,55],[37,56],[15,57],[29,58],[39,59],[7,60],[59,61],[56,62],[59,63],[31,64],[9,65],[9,66],[12,67],[66,68],[19,69],[14,70],[69,71],[35,72],[12,73],[2,74],[66,75],[28,76],[69,77],[45,78],[11,79],[55,80],[79,81],[78,82],[6,83],[76,84],[79,85],[14,86],[44,87],[7,88],[19,89],[60,90],[49,91],[46,92],[23,93],[34,94],[18,95],[26,96],[26,97],[95,98],[63,99],[59,100],[40,101],[56,102],[29,103],[33,104],[74,105],[79,106],[70,107],[25,108],[76,109],[69,110],[6,111],[25,112],[88,113],[112,114],[87,115],[97,116],[27,117],[45,118],[51,119],[95,120],[74,121],[111,122],[43,123],[94,124],[46,125],[50,126],[77,127],[26,128],[34,129],[35,130],[84,131],[29,132],[20,133],[6,134],[131,135],[64,136],[87,137],[69,138],[123,139],[100,140],[69,141],[91,142],[60,143],[120,144],[114,145],[123,146],[22,147],[1,148],[80,149],[109,150],[55,151],[97,152],[135,153],[135,154],[32,155],[42,156],[27,157],[32,158],[59,159],[36,160],[105,161],[93,162],[1,163],[129,164],[28,165],[154,166],[106,167],[2,168],[46,169],[44,170],[147,171],[3,172],[31,173],[49,174],[83,175],[39,176],[42,177],[112,178],[3,179],[1,180],[103,181],[69,182],[119,183],[97,184],[150,185],[61,186],[84,187],[104,188],[36,189],[69,190],[181,191],[8,192],[182,193],[158,194],[148,195],[94,196],[17,197],[95,198],[86,199],[37,200],[181,201],[112,202],[155,203],[76,204],[73,205],[186,206],[186,207],[92,208],[129,209],[22,210],[195,211],[185,212],[202,213],[49,214],[113,215],[156,216],[77,217],[121,218],[98,219],[45,220],[75,221],[154,222],[195,223],[59,224],[104,225],[62,226],[134,227],[9,228],[158,229],[71,230],[120,231],[156,232],[125,233],[12,234],[109,235],[167,236],[172,237],[62,238],[131,239],[234,240],[237,241],[187,242],[224,243],[224,244],[31,245],[159,246],[28,247],[132,248],[123,249],[88,250],[63,251],[228,252],[100,253],[147,254],[228,255],[111,256],[19,257],[235,258],[20,259],[30,260],[149,261],[60,262],[20,263],[43,264],[160,265],[83,266],[108,267],[81,268],[63,269],[89,270],[24,271],[261,272],[179,273],[52,274],[114,275],[219,276],[259,277],[239,278],[274,279],[39,280],[53,281],[161,282],[256,283],[219,284],[229,285],[159,286],[143,287],[286,288],[195,289],[99,290],[25,291],[244,292],[134,293],[286,294],[163,295],[174,296],[184,297],[171,298],[158,299],[10,300],[269,301],[233,302],[220,303],[50,304],[222,305],[220,306],[263,307],[266,308],[7,309],[117,310],[191,311],[207,312],[302,313],[9,314],[193,315],[219,316],[185,317],[120,318],[176,319],[119,320],[130,321],[233,322],[160,323],[56,324],[303,325],[167,326],[236,327],[97,328],[61,329],[20,330],[242,331],[90,332],[169,333],[332,334],[298,335],[291,336],[205,337],[74,338],[173,339],[257,340],[9,341],[39,342],[263,343],[10,344],[78,345],[29,346],[322,347],[43,348],[134,349],[344,350],[327,351],[270,352],[21,353],[345,354],[277,355],[158,356]])
print(x)
# min_tree(3,[[1, 2], [2, 3], [3, 1],[3,5],[5,6],[6,3]])