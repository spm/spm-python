import unittest
import numpy as np
import itertools

from spm import StructArray, Struct

class StructArrayTestCase(unittest.TestCase):
    def setUp(self):
        # Prepare some example data for testing
        self.struct1 = {'a': 1, 'b': 2}
        self.struct2 = {'a': 2, 'c': 4}
        self.struct3 = {'a': 3, 'c': 5}
        self.struct4 = {'a': 4, 'b': 1}
        self.array1d = [self.struct1, self.struct2]
        self.array2d = np.array([[self.struct1, self.struct2], [self.struct3, self.struct4]])

    def test_initialization_with_structs(self):
        sa = StructArray(self.array1d)
        self.assertEqual(sa._structs.shape, (1, len(self.array1d)))

    def test_initialization_with_ndarray(self):
        sa = StructArray(self.array2d)
        self.assertEqual(sa._structs.shape, self.array2d.shape)

    def test_getitem(self):
        sa = StructArray(self.array1d)
        struct = sa[1]
        self.assertIsInstance(struct, dict)
        self.assertEqual(struct, self.struct2)

    def test_keys(self):
        sa = StructArray(self.array2d)
        keys = sa.keys()
        self.assertEqual(keys, {'a', 'b', 'c'})

    def test_as_matlab_object(self):
        sa = StructArray(self.array2d)
        objdict = sa._as_matlab_object()
        self.assertEqual(objdict['type__'], 'structarray')
        self.assertEqual(objdict['size__'].reshape(-1).tolist(), list(self.array2d.shape))
        self.assertEqual(len(objdict['data__']), self.array2d.size)

    def test_from_matlab_object(self):
        sa = StructArray(self.array2d)
        objdict = sa._as_matlab_object()
        reconstructed_sa = StructArray._from_matlab_object(objdict)
        self.assertEqual(reconstructed_sa._structs.shape, sa._structs.shape)
        self.assertEqual(reconstructed_sa.keys(), sa.keys())

    def test_with_struct(self):
        sa = StructArray(list(map(Struct, self.array1d)))
        objdict = sa._as_matlab_object()
        reconstructed_sa = StructArray._from_matlab_object(objdict)

    def test_flat_shape(self):
        sa = StructArray(self.array2d)
        objdict = sa._as_matlab_object()
        self.assertEqual(len(objdict['data__']), 4)
        self.assertEqual(objdict['data__'][0]['a'], self.struct1['a'])
        self.assertEqual(objdict['data__'][1]['a'], self.struct3['a'])
        self.assertEqual(objdict['data__'][2]['a'], self.struct2['a'])
        self.assertEqual(objdict['data__'][3]['a'], self.struct4['a'])

    def test_repr(self):
        sa = StructArray(self.array1d)
        repr_str = repr(sa)
        self.assertIn('StructArray', repr_str)
        self.assertIn('keys', repr_str)

    def test_invalid_initialization(self):
        with self.assertRaises(TypeError):
            StructArray(123)

        with self.assertRaises(TypeError):
            StructArray(['not', 'a', 'dict'])

    def test_empty_structarray(self):
        sa = StructArray()
        self.assertEqual(sa._structs.size, 0)
        self.assertEqual(len(sa.keys()), 0)


if __name__ == '__main__':
    unittest.main()