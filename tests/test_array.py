import unittest
import numpy as np

from spm import Runtime, Array


class CellTestCase(unittest.TestCase):

    def test_instantiate_empty(self):
        a = Array()
        self.assertIsInstance(a, Array)
        self.assertEqual(a.shape, ())
        self.assertEqual(a.dtype, np.float64)

    def test_instantiate_shape_1d(self):
        a = Array([3])
        self.assertIsInstance(a, Array)
        self.assertEqual(a.shape, (3,))
        self.assertEqual(a.dtype, np.float64)
        self.assertTrue((a == 0).all())

    def test_instantiate_shape_2d(self):
        a = Array([3, 2])
        self.assertIsInstance(a, Array)
        self.assertEqual(a.shape, (3, 2))
        self.assertTrue((a == 0).all())

    def test_instantiate_shape_order(self):
        a = Array([3, 2], order="C")
        self.assertIsInstance(a, Array)
        self.assertEqual(a.shape, (3, 2))
        self.assertEqual(a.strides, (2*8, 8))

        a = Array([3, 2], order="F")
        self.assertIsInstance(a, Array)
        self.assertEqual(a.shape, (3, 2))
        self.assertEqual(a.strides, (8, 8*3))

    def test_as_struct(self):
        self.assertRaises(TypeError, lambda: Array().as_struct)

    def test_as_num(self):
        a = Array()
        self.assertTrue(a.as_num is a)

    def test_as_cell(self):
        self.assertRaises(TypeError, lambda: Array().as_cell)

    def test_rowvec_from_matlab(self):
        c_matlab = Runtime.call("eval", "[1, 2, 3]")
        c_python = Array.from_any([[1, 2, 3]])
        self.assertListEqual(c_matlab.tolist(), c_python.tolist())

    def test_colvec_from_matlab(self):
        c_matlab = Runtime.call("eval", "[1; 2; 3]")
        c_python = Array.from_any([[1], [2], [3]])
        self.assertListEqual(c_matlab.tolist(), c_python.tolist())

    def test_array2d_from_matlab(self):
        c_matlab = Runtime.call("eval", "[1, 2, 3; 4, 5, 6]")
        c_python = Array.from_any([[1, 2, 3], [4, 5, 6]])
        self.assertTrue(c_matlab.tolist() == c_python.tolist())

    def test_append_1d(self):
        a = Array.from_any([1, 2, 3], owndata=True)
        a.append(4)
        self.assertListEqual(a.tolist(), [1, 2, 3, 4])

    def test_extend_1d(self):
        a = Array.from_any([1, 2, 3], owndata=True)
        a.extend([4, 5])
        self.assertListEqual(a.tolist(), [1, 2, 3, 4, 5])

        a = Array.from_any([1, 2, 3], owndata=True)
        a.extend(Array.from_any([4, 5]))
        self.assertListEqual(a.tolist(), [1, 2, 3, 4, 5])

    def test_extend_2d(self):
        a = Array.from_any([[1, 2, 3], [4, 5, 6]], owndata=True)
        a.extend(Array.from_any([[7, 8, 9]]))
        self.assertListEqual(a.tolist(), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def test_indexing_1d(self):
        a = Array.from_any([1, 2, 3], owndata=True)

        # __getitem__
        self.assertEqual(a[1], 2)
        self.assertEqual(a[-1], 3)
        self.assertEqual(a[1:].tolist(), [2, 3])
        self.assertEqual(a[[0, 2]].tolist(), [1, 3])

        # __setitem__
        a[1] = 4
        self.assertEqual(a.tolist(), [1, 4, 3])
        a[-1] = 5
        self.assertEqual(a.tolist(), [1, 4, 5])
        a[1:] = [2, 3]
        self.assertEqual(a.tolist(), [1, 2, 3])
        a[[0, 2]] = [7, 8]
        self.assertEqual(a.tolist(), [7, 2, 8])
        a[3] = 9  # insert new element
        self.assertEqual(a.tolist(), [7, 2, 8, 9])
        a[5] = 11  # insert new element
        self.assertEqual(a.tolist(), [7, 2, 8, 9, 0, 11])

        # __delitem__
        del a[4]
        self.assertEqual(a.tolist(), [7, 2, 8, 9, 11])
        del a[-2:]
        self.assertEqual(a.tolist(), [7, 2, 8])
        del a[[0, 2]]
        self.assertEqual(a.tolist(), [2])

    def test_roundtrip_1d(self):
        a = Array.from_any([1, 2, 3])
        identity = Runtime.call('eval',  '@(x) x')
        a = Array.from_any([[1, 2, 3]])
        d = identity(a)
        self.assertListEqual(a.tolist(), d.tolist())

    def test_roundtrip_2d(self):
        identity = Runtime.call('eval',  '@(x) x')
        a = Array.from_any([[1, 2, 3], [3, 4, 5]])
        d = identity(a)
        self.assertListEqual(a.tolist(), d.tolist())


if __name__ == '__main__':
    unittest.main()
