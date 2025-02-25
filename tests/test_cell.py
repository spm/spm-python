import unittest
import numpy as np

from spm import Cell, Runtime


class CellTestCase(unittest.TestCase):

    def test_instantiate_empty(self):
        c = Cell()
        a = np.asarray([])
        self.assertIsInstance(c, Cell)
        self.assertListEqual(c.tolist(), a.tolist())

    def test_instantiate_shape_1d(self):
        c = Cell([3])
        self.assertIsInstance(c, Cell)
        self.assertEqual(c.shape, (3,))
        self.assertTrue(all(x.shape == (0,) for x in c))

    def test_instantiate_shape_2d(self):
        c = Cell([3, 2])
        self.assertIsInstance(c, Cell)
        self.assertEqual(c.shape, (3, 2))
        self.assertTrue(all(x.shape == (0,) for x in c.flat))

    def test_instantiate_shape_order(self):
        c = Cell([3, 2], order="C")
        self.assertIsInstance(c, Cell)
        self.assertEqual(c.shape, (3, 2))
        self.assertEqual(c.strides, (2*8, 8))

        c = Cell([3, 2], order="F")
        self.assertIsInstance(c, Cell)
        self.assertEqual(c.shape, (3, 2))
        self.assertEqual(c.strides, (8, 8*3))

    def test_instantiate_list(self):
        c = Cell.from_any(['a', 'b', 'c'])
        self.assertEqual(c.shape, (3,))
        self.assertEqual(repr(c), "Cell(['a', 'b', 'c'])")
        self.assertListEqual(c.tolist(), ['a', 'b', 'c'])

    def test_instantiate_nested_list(self):
        c = Cell.from_any([['a', 'b'], ['c', 'd']])
        self.assertEqual(c.shape, (2,))
        self.assertEqual(repr(c), "Cell([Cell(['a', 'b']), Cell(['c', 'd'])])")
        self.assertTrue(all(isinstance(x, Cell) for x in c.tolist()))

    def test_instantiate_nested_list_deepcat(self):
        c = Cell.from_any([['a', 'b'], ['c', 'd']], deepcat=True)
        self.assertEqual(c.shape, (2, 2))
        self.assertEqual(repr(c), "Cell([['a', 'b'],\n      ['c', 'd']])")
        self.assertTrue(all(isinstance(x, list) for x in c.tolist()))

    def test_as_struct(self):
        self.assertRaises(TypeError, lambda: Cell().as_struct)

    def test_as_num(self):
        self.assertRaises(TypeError, lambda: Cell().as_num)

    def test_as_cell(self):
        c = Cell()
        self.assertTrue(c.as_cell is c)

    def test_cell1d_from_matlab(self):
        c_matlab = Runtime.call("eval", "{1, 2, 3}")
        c_python = Cell.from_any([1, 2, 3])
        self.assertListEqual(c_matlab.tolist(), c_python.tolist())

    def test_cell2d_from_matlab(self):
        c_matlab = Runtime.call("eval", "{1, 2, 3; 4, 5, 6}")
        c_python = Cell.from_any([[1, 2, 3], [4, 5, 6]], deepcat=True)
        self.assertTrue(c_matlab.tolist() == c_python.tolist())

    def test_nested_cell_from_matlab(self):
        c_matlab = Runtime.call("eval", "{{1, 2, 3}, {4, 5, 6}}")
        c_python = Cell.from_any([[1, 2, 3], [4, 5, 6]])
        c_matlab = [x.tolist() for x in c_matlab.tolist()]
        c_python = [x.tolist() for x in c_python.tolist()]
        self.assertListEqual(c_matlab, c_python)
