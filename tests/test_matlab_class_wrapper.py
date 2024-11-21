import unittest
import warnings
import numpy as np
from unittest.mock import patch, MagicMock

from spm.__wrapper__ import MatlabClassWrapper, Runtime


orig_runtime_call = Runtime.call
def mock_runtime_call(f, *args, **kwargs):
    if f == 'TestClass':
        objdict = {
            'type__': 'object', 
            'class__': 'TestClass', 
            'data__': kwargs
        }
        return Runtime._process_argout(objdict)
    if f == 'str2func':
        return ''
    else:
        return orig_runtime_call(f, *args, **kwargs)


@patch('spm.__wrapper__.Runtime.call', mock_runtime_call)
class TestMatlabClassWrapper(unittest.TestCase):
    def setUp(self):

        # Example subclass for testing
        class TestClass(MatlabClassWrapper):
            def __init__(self, *args, **kwargs):
                super().__init__()

            def subsref(self, ref):
                if ref['type'] == '.':
                    return self._objdict[ref['subs']-1]
                elif ref['type'] in ('()', '{}'):
                    if isinstance(ref['subs'], tuple):
                        ref['subs'] = ref['subs'][0]
                    return self._objdict['data__']['value'][ref['subs']-1]
                else:
                    raise KeyError("Unsupported reference type.")

            def subsasgn(self, ref, value):
                if ref['type'] == '.':
                    self._objdict[ref['subs']-1] = value
                elif ref['type'] in ('()', '{}'):
                    self._objdict['data__']['value'][ref['subs']-1] = value
                else:
                    raise KeyError("Unsupported assignment type.")

        self.TestClass = TestClass

    def test_subclass_registration(self):
        self.assertIn('TestClass', MatlabClassWrapper._subclasses)
        self.assertIs(MatlabClassWrapper._subclasses['TestClass'], self.TestClass)

    def test_object_creation(self):
        obj = self.TestClass(value=[1, 2, 3])
        self.assertEqual(obj._objdict['class__'], 'TestClass')
        self.assertEqual(obj._objdict['data__']['value'], [1, 2, 3])

    def test_from_matlab_object(self):
        objdict = {'class__': 'TestClass', 'data__': {'value':[1, 2, 3]}}
        obj = MatlabClassWrapper._from_matlab_object(objdict)
        self.assertIsInstance(obj, self.TestClass)
        self.assertEqual(obj._objdict['data__']['value'], [1, 2, 3])

    def test_unknown_class_warning(self):
        objdict = {'class__': 'UnknownClass', 'data__': {'value': [1, 2, 3]}}
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            obj = MatlabClassWrapper._from_matlab_object(objdict)
            self.assertEqual(len(w), 1)
            self.assertEqual(str(w[0].message), 'Unknown Matlab class type: UnknownClass')
        self.assertIsInstance(obj, MatlabClassWrapper)

    def test_attribute_access(self):
        obj = self.TestClass(value=[1, 2, 3])
        self.assertEqual(obj._objdict['data__']['value'], [1, 2, 3])

    def test_item_get_and_set(self):
        obj = self.TestClass(value=[1, 2, 3])
        self.assertEqual(obj[1], 2)  # Testing __getitem__
        obj[1] = 5                  # Testing __setitem__
        self.assertEqual(obj[1], 5)

    def test_call_behavior(self):
        obj = self.TestClass(value=[1, 2, 3])
        self.assertEqual(obj(0), 1)  # Testing __call__

    def test_as_matlab_object(self):
        obj = self.TestClass(value=[1, 2, 3])
        objdict = obj._as_matlab_object()
        self.assertEqual(objdict['class__'], 'TestClass')
        self.assertEqual(objdict['data__']['value'], [1, 2, 3])

    def test_index_processing(self):
        obj = self.TestClass(value=np.arange(10))
        index = obj._process_index(slice(1, 5))
        self.assertTrue(np.array_equal(index, np.array([2, 3, 4, 5])))

    def test_invalid_index(self):
        obj = self.TestClass(value=np.arange(10))
        with self.assertRaises(IndexError):
            obj[15]


if __name__ == '__main__':
    unittest.main()
