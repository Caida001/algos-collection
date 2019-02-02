Given the head of a graph, return a deep copy (clone) of the graph. Each node in the graph contains a label (int) and a list (List[UndirectedGraphNode]) of its neighbors. There is an edge between the given node and each of the nodes in its neighbors.


OJ's undirected graph serialization (so you can understand error output):
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
 

As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
 

Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/



class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    def cloneGraph(self, node):
        if not node: return 
        nodeCopy = UndirectedGraphNode(node.label)
        queue = collections.deque([node])
        dic = {node: nodeCopy}
        while queue: 
            curNode = queue.popleft()
            for neighbor in curNode.neighbors:
                if neighbor not in dic:
                    NeighborCopy = UndirectedGraphNode(neighbor.label)
                    dic[neighbor] = NeighborCopy
                    dic[curNode].neighbors.append(NeighborCopy)
                    queue.append(neighbor)
                else:
                    dic[curNode].neighbors.append(dic[neighbor])

        return nodeCopy   


class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
      if not node: return 
      nodeCopy = UndirectedGraphNode(node.label)
      dic = {node: nodeCopy}
      stack = [node]
      while stack:
        curNode = stack.pop()
        for neighbor in curNode.neighbors:
          if neighbor not in dic:
            neighborCopy = UndirectedGraphNode(neighbor.label)
            dic[neighbor] = neighborCopy 
            dic[curNode].neighbors.append(neighborCopy)
            stack.append(neighbor)
          else:
            dic[curNode].neighbors.append(dic[neighbor])
            
      return nodeCopy




class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
      if not node: return 
      nodeCopy = UndirectedGraphNode(node.label)
      dic = {node: nodeCopy}
      self.dfs(node, dic)    
      return nodeCopy
    
    
    def dfs(self, curNode, dic):
      for neighbor in curNode.neighbors:
        if neighbor not in dic:
          neighborCopy = UndirectedGraphNode(neighbor.label)
          dic[neighbor] = neighborCopy 
          dic[curNode].neighbors.append(neighborCopy)
          self.dfs(neighbor, dic)
        else:
          dic[curNode].neighbors.append(dic[neighbor])

