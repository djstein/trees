def bfs(data, searchVal):
    stack = [data]
    while len(stack):
        print(stack)
        node = stack.pop(0)
        print(node)
        if searchVal in node.get("data"):
            return node
        else:
            stack.extend([val for val in node.get("children").values()])


def test_bfs():
    node_1 = {"children": {}, "data": "can do"}
    node_2 = {"children": {}, "data": "wow"}
    node_0 = {"children": {"1": node_1, "2": node_2}, "data": "hello world"}

    searchVal = "wow"
    return_node = bfs(node_0, searchVal)
    print(return_node)
    assert node_2 == bfs(node_0, searchVal)


def test_bfs_depth():
    node_4 = {"children": {}, "data": "the real input"}
    node_3 = {"children": {"4": node_4}, "data": "testing here"}

    node_1 = {"children": {}, "data": "can do"}
    node_2 = {"children": {"3": node_3}, "data": "wow"}
    node_0 = {"children": {"1": node_1, "2": node_2}, "data": "hello world"}

    searchVal = "the real input"
    return_node = bfs(node_0, searchVal)
    print(return_node)
    assert node_4 == return_node
