from collections import deque


def breadthFirstSearch(firstNode, targetNode, graph):
    '''图的广度优先搜索.

    运用队列按层彻底地搜索整张图

    Args:
        firstNode: 起始节点.
        targetNode: 目标节点.
        graph: 给定图.

    Returns:
        如果该节点存在则返回True,不存在则返回False.
        Forexample:
        print(breadthFirstSearch("Rainbow", "Glaz", test_graph))
        #True
        print(breadthFirstSearch("Rainbow", "Fuze", test_graph))
        #False

    Raises:
        IOError: .
    '''    
    searchDeque = deque()
    searchDeque += graph[firstNode]
    isSearched = []  # 这个数组记录已经搜索过的节点
    while searchDeque:
        node = searchDeque.popleft()
        if node not in isSearched:
            if node == targetNode:
                print("存在此人:"+targetNode)
                return True
            else:
                searchDeque += graph[node]
                isSearched.append(node)
    print("查无此人:"+targetNode)
    return False


test_graph = {}
test_graph["Rainbow"] = ["Ash", "Mute", "Echo"]
test_graph["Ash"] = ["Castle", "Thermite"]
test_graph["Mute"] = ["Sledge","Ash"]
test_graph["Echo"] = ["Hibana", "Ying"]
test_graph["Castle"] = ["Glaz"]
test_graph["Thermite"] = []
test_graph["Sledge"] = []
test_graph["Hibana"] = []
test_graph["Ying"] = []
test_graph["Glaz"] = []

print(breadthFirstSearch("Rainbow", "Glaz", test_graph))
print(breadthFirstSearch("Rainbow", "Fuze", test_graph))
