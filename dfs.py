import unittest


class Node:
    def __init__(self, name, data, children=[]):
        self.name = name
        self.children = children
        self.data = data


def dfs_search(tree, search):
    stack = [tree]
    trace = []
    while stack:
        node = stack.pop(0)
        trace.append(node.name)
        if node.data == search:
            return node, trace
        elif node.children:
            for child in node.children[::-1]:
                stack.insert(0, child)


class DFSTest(unittest.TestCase):
    def setUp(self):
        self.node_5 = Node(name="5", data="the real input")
        node_3 = Node(name="3", data="testing here")
        node_6 = Node(name="6", data="general")
        node_4 = Node(name="4", children=[node_6], data="can do")
        node_2 = Node(name="2", children=[self.node_5], data="wow")
        self.node_1 = Node(name="1", children=[node_3, node_4], data="hello there")
        self.node_0 = Node(name="0", children=[self.node_1, node_2], data="hello world")
        self.tree = self.node_0

    def test_first_value(self):
        search = "hello world"
        results = dfs_search(self.tree, search)
        self.assertTrue(results[0].data)
        self.assertEqual(self.node_0, results[0])
        track = ["0"]
        self.assertEqual(track, results[1])
        print(results[1])

    def test_last_value(self):
        search = "the real input"
        results = dfs_search(self.tree, search)
        self.assertTrue(results[0].data)
        self.assertEqual(self.node_5, results[0])
        track = ["0", "1", "3", "4", "6", "2", "5"]
        self.assertEqual(track, results[1])
        print(results[1])


if __name__ == "__main__":
    unittest.main()
