import unittest


class Node:
    def __init__(self, name, data, children=[]):
        self.name = name
        self.children = children
        self.data = data


def drf_search(tree, search):
    track = []
    stack = [tree]
    while len(stack):
        node = stack.pop(0)
        track.extend(node.name)
        children = node.children
        if search in node.data:
            return node, track
        elif children:
            stack.extend(children)


class DRFTest(unittest.TestCase):
    def setUp(self):
        self.node_4 = Node(name="4", data="the real input")
        node_3 = Node(name="3", children=[self.node_4], data="testing here")
        node_1 = Node(name="1", data="can do")
        node_2 = Node(name="2", children=[node_3], data="wow")
        self.node_0 = Node(name="0", children=[node_1, node_2], data="hello world")
        self.tree = self.node_0

    def test_find_apex_value(self):
        search = "hello world"
        results = drf_search(self.tree, search)
        self.assertTrue(results[0].data)
        self.assertEqual(self.node_0, results[0])
        track = ["0"]
        self.assertEqual(track, results[1])

    def test_find_last_value(self):
        search = "the real input"
        results = drf_search(self.tree, search)
        self.assertTrue(results[0].data)
        self.assertEqual(self.node_4, results[0])
        track = ["0", "1", "2", "3", "4"]
        self.assertEqual(track, results[1])


if __name__ == "__main__":
    unittest.main()
