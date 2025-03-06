import unittest
import numpy as np

from spm import Cell, Runtime, Array


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

    def test_empty1d_row_from_matlab(self):
        c_matlab = Runtime.call("cell", 1, 3)
        c_python = Cell.from_shape([3])
        self.assertListEqual(c_matlab.tolist(), c_python.tolist())

    def test_empty1d_col_from_matlab(self):
        c_matlab = Runtime.call("cell", 3, 1)
        c_python = Cell.from_shape([3, 1])
        self.assertListEqual(c_matlab.tolist(), c_python.tolist())

    def test_empty2d_from_matlab(self):
        c_matlab = Runtime.call("cell", 3, 2)
        c_python = Cell.from_shape([3, 2])
        self.assertListEqual(c_matlab.tolist(), c_python.tolist())

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

    def test_append_1d(self):
        c = Cell.from_any([1, 2, 3], owndata=True)
        c.append(4)
        self.assertListEqual(c.tolist(), [1, 2, 3, 4])

    def test_extend_1d(self):
        c = Cell.from_any([1, 2, 3], owndata=True)
        c.extend([4, 5])
        self.assertListEqual(c.tolist(), [1, 2, 3, 4, 5])

        c = Cell.from_any([1, 2, 3], owndata=True)
        c.extend(Cell.from_any([4, 5]))
        self.assertListEqual(c.tolist(), [1, 2, 3, 4, 5])

    def test_extend_magic(self):
        # iadd
        c = Cell.from_any([1, 2, 3], owndata=True)
        c += [4, 5]
        self.assertListEqual(c.tolist(), [1, 2, 3, 4, 5])

        # add
        c = Cell.from_any([1, 2, 3], owndata=True)
        c = c + [4, 5]
        self.assertListEqual(c.tolist(), [1, 2, 3, 4, 5])

        # radd
        c = Cell.from_any([1, 2, 3], owndata=True)
        c = [4, 5] + c
        self.assertListEqual(c.tolist(), [4, 5, 1, 2, 3])

        # imul
        c = Cell.from_any([1, 2, 3], owndata=True)
        c *= 2
        self.assertListEqual(c.tolist(), [1, 2, 3, 1, 2, 3])

        # mul
        c = Cell.from_any([1, 2, 3], owndata=True)
        c = c * 2
        self.assertListEqual(c.tolist(), [1, 2, 3, 1, 2, 3])

        # rmul
        c = Cell.from_any([1, 2, 3], owndata=True)
        c = 2 * c
        self.assertListEqual(c.tolist(), [1, 2, 3, 1, 2, 3])

    def test_extend_2d(self):
        c = Cell.from_any([[1, 2, 3], [4, 5, 6]], owndata=True, deepcat=True)
        c.extend(Cell.from_any([[7, 8, 9]], deepcat=True))
        self.assertListEqual(c.tolist(), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def test_list_api_1d(self):
        c = Cell.from_any([1, 2, 3], owndata=True)
        self.assertEqual(c.count(1), 1)
        self.assertEqual(c.count(4), 0)
        self.assertEqual(c.index(1), 0)
        self.assertRaises(ValueError, lambda: c.index(4))
        c.remove(2)
        self.assertListEqual(c.tolist(), [1, 3])
        self.assertRaises(ValueError, lambda: c.remove(4))
        c.insert(-1, 4)
        self.assertListEqual(c.tolist(), [1, 3, 4])
        c.insert(1, 2)
        self.assertListEqual(c.tolist(), [1, 2, 3, 4])
        b = c.pop()
        self.assertListEqual(c.tolist(), [1, 2, 3])
        self.assertEqual(b, 4)
        b = c.pop(0)
        self.assertListEqual(c.tolist(), [2, 3])
        self.assertEqual(b, 1)
        c.reverse()
        self.assertListEqual(c.tolist(), [3, 2])
        c.sort()
        self.assertListEqual(c.tolist(), [2, 3])

    def test_list_api_2d(self):
        c = Cell.from_any([[1, 2, 3], [4, 5, 6]], owndata=True, deepcat=True)
        self.assertEqual(c.count([4, 5, 6]), 1)
        self.assertEqual(c.count([4, 4, 4]), 0)
        self.assertEqual(c.index([4, 5, 6]), 1)
        self.assertRaises(ValueError, lambda: c.index([4, 4, 4]))
        c.remove([4, 5, 6])
        self.assertListEqual(c.tolist(), [[1, 2, 3]])
        self.assertRaises(ValueError, lambda: c.remove([4, 4, 4]))
        c.insert(-1, [4, 5, 6])
        self.assertListEqual(c.tolist(), [[1, 2, 3], [4, 5, 6]])
        c.insert(1, [7, 8, 9])
        self.assertListEqual(c.tolist(), [[1, 2, 3], [7, 8, 9], [4, 5, 6]])
        b = c.pop()
        self.assertListEqual(c.tolist(), [[1, 2, 3], [7, 8, 9]])
        self.assertEqual(b.tolist(), [4, 5, 6])
        b = c.pop(0)
        self.assertListEqual(c.tolist(), [[7, 8, 9]])
        self.assertEqual(b.tolist(), [1, 2, 3])

        c = Cell.from_any(
            [[1, 9, 5],
             [4, 2, 6],
             [3, 7, 8]],
            owndata=True, deepcat=True)
        self.assertListEqual(c.tolist(), [[1, 9, 5], [4, 2, 6], [3, 7, 8]])
        c.reverse()
        self.assertListEqual(c.tolist(), [[3, 7, 8], [4, 2, 6], [1, 9, 5]])
        c.sort()
        self.assertListEqual(c.tolist(), [[1, 2, 5], [3, 7, 6], [4, 9, 8]])

    def test_indexing_1d(self):
        c = Cell.from_any([1, 2, 3], owndata=True)

        # __getitem__
        self.assertEqual(c[1], 2)
        self.assertEqual(c[-1], 3)
        self.assertEqual(c[1:].tolist(), [2, 3])
        self.assertEqual(c[[0, 2]].tolist(), [1, 3])

        # __setitem__
        c[1] = 4
        self.assertEqual(c.tolist(), [1, 4, 3])
        c[-1] = 5
        self.assertEqual(c.tolist(), [1, 4, 5])
        c[1:] = [2, 3]
        self.assertEqual(c.tolist(), [1, 2, 3])
        c[[0, 2]] = [7, 8]
        self.assertEqual(c.tolist(), [7, 2, 8])
        c[3] = 9  # insert new element
        self.assertEqual(c.tolist(), [7, 2, 8, 9])
        c[5] = 11  # insert new element
        self.assertTrue(isinstance(c[4], Array) and c[4].shape == (0,))
        self.assertTrue(c[5] == 11)

        # __delitem__
        del c[4]
        self.assertEqual(c.tolist(), [7, 2, 8, 9, 11])
        del c[-2:]
        self.assertEqual(c.tolist(), [7, 2, 8])
        del c[[0, 2]]
        self.assertEqual(c.tolist(), [2])

    def test_roundtrip_1d(self):
        identity = Runtime.call('eval',  '@(x) x')
        c = Cell.from_any([1, 2, 3])
        d = identity(c)
        self.assertListEqual(c.tolist(), d.tolist())

    def test_roundtrip_2d(self):
        identity = Runtime.call('eval',  '@(x) x')
        c = Cell.from_any([[1, 2, 3], [3, 4, 5]], deepcat=True)
        d = identity(c)
        self.assertListEqual(c.tolist(), d.tolist())


if __name__ == '__main__':
    unittest.main()
