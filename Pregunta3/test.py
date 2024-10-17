import unittest
from Classes import *

class TestClasses(unittest.TestCase):
    '''
    Use of unittest to test all the calsses
    '''
    def setUp(self):
        # Create vertices
        self.v1 = Vertex('A', 0)
        self.v2 = Vertex('B', 1)
        self.v3 = Vertex('C', 2)
        self.vertices = [self.v1, self.v2, self.v3]

        # Create graph
        self.graph = Graph(self.vertices)

    def test_vertex_creation(self):
        self.assertEqual(self.v1.data, 'A')
        self.assertEqual(self.v1.number, 0)

    def test_edge_creation(self):
        edge = Edge(self.v1, self.v2)
        self.assertEqual(edge.v1, self.v1)
        self.assertEqual(edge.v2, self.v2)

    def test_graph_creation(self):
        self.assertEqual(self.graph.verticesNumber, 3)
        self.assertEqual(len(self.graph.Edges), 0)
        self.assertEqual(len(self.graph.adyacencies[self.v1]), 0)

    def test_add_edge(self):
        self.graph.addEdge(self.v1, self.v2)
        self.assertEqual(len(self.graph.Edges), 1)
        self.assertIn(self.v2, self.graph.adyacencies[self.v1])

    def test_bfs(self):
        self.graph.addEdge(self.v1, self.v2)
        self.graph.addEdge(self.v2, self.v3)
        self.assertTrue(self.graph.BFS(self.v1, 'C'))
        self.assertFalse(self.graph.BFS(self.v1, 'D'))

class TestInterpreter(unittest.TestCase):

    def setUp(self):
        self.interpreter = Interpreter('Python', 'English')

    def test_interpreter_creation(self):
        self.assertEqual(self.interpreter.language, 'English')
        self.assertEqual(self.interpreter.languageInter, 'Python')

class TestProgram(unittest.TestCase):

    def setUp(self):
        self.program = Program('MyApp', 'Python')

    def test_program_creation(self):
        self.assertEqual(self.program.name, 'MyApp')
        self.assertEqual(self.program.language, 'Python')

class TestTranslator(unittest.TestCase):

    def setUp(self):
        self.translator = Translator('Google Translate', 'English', 'Spanish')

    def test_translator_creation(self):
        self.assertEqual(self.translator.languageTrans, 'Google Translate')
        self.assertEqual(self.translator.languageFrom, 'English')
        self.assertEqual(self.translator.languageTo, 'Spanish')

if __name__ == '__main__':
    unittest.main()
