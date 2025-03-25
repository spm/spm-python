import unittest
import warnings
import numpy as np
from unittest.mock import patch

from spm import Runtime, MatlabClass


orig_runtime_call = Runtime.call


def mock_runtime_call(f, *args, **kwargs):
    if f == "TestClass":
        objdict = {"type__": "object", "class__": "TestClass", "data__": kwargs}
        return Runtime._process_argout(objdict)
    if f == "str2func":
        return ""
    else:
        return orig_runtime_call(f, *args, **kwargs)


@patch("spm.Runtime.call", mock_runtime_call)
class TestMatlabClass(unittest.TestCase):
    def setUp(self):
        # Example subclass for testing
        class TestClass(MatlabClass):
            def __init__(self, *args, **kwargs):
                super().__init__()

            def subsref(self, ref):
                if ref["type"] == ".":
                    return self._objdict[ref["subs"] - 1]
                elif ref["type"] in ("()", "{}"):
                    if isinstance(ref["subs"], tuple):
                        ref["subs"] = ref["subs"][0]
                    return self._objdict["data__"]["value"][ref["subs"] - 1]
                else:
                    raise KeyError("Unsupported reference type.")

            def subsasgn(self, ref, value):
                if ref["type"] == ".":
                    self._objdict[ref["subs"] - 1] = value
                elif ref["type"] in ("()", "{}"):
                    self._objdict["data__"]["value"][ref["subs"] - 1] = value
                else:
                    raise KeyError("Unsupported assignment type.")

        self.TestClass = TestClass

    def test_matlabclass_register_subclass(self):
        self.assertIn("TestClass", MatlabClass._subclasses)
        self.assertIs(MatlabClass._subclasses["TestClass"], self.TestClass)

    def test_matlabclass_instantiate_object(self):
        obj = self.TestClass(value=[1, 2, 3])
        self.assertEqual(obj._objdict["class__"], "TestClass")
        self.assertEqual(obj._objdict["data__"]["value"], [1, 2, 3])

    def test_matlabclass_from_matlab_object(self):
        objdict = {"class__": "TestClass", "data__": {"value": [1, 2, 3]}}
        obj = MatlabClass._from_runtime(objdict)
        self.assertIsInstance(obj, self.TestClass)
        self.assertEqual(obj._objdict["data__"]["value"], [1, 2, 3])

    def test_matlabclass_unknown_class_warning(self):
        objdict = {"class__": "UnknownClass", "data__": {"value": [1, 2, 3]}}
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            obj = MatlabClass._from_runtime(objdict)
            self.assertEqual(len(w), 1)
            self.assertEqual(
                str(w[0].message), "Unknown Matlab class type: UnknownClass"
            )
        self.assertIsInstance(obj, MatlabClass)

    def test_matlabclass_attribute_access(self):
        obj = self.TestClass(value=[1, 2, 3])
        self.assertEqual(obj._objdict["data__"]["value"], [1, 2, 3])

    def test_matlabclass_item_get_and_set(self):
        obj = self.TestClass(value=[1, 2, 3])
        self.assertEqual(obj[1], 2)  # Testing __getitem__
        obj[1] = 5  # Testing __setitem__
        self.assertEqual(obj[1], 5)

    def test_matlabclass_call_behavior(self):
        obj = self.TestClass(value=[1, 2, 3])
        self.assertEqual(obj(0), 1)  # Testing __call__

    def test_matlabclass_as_matlab_object(self):
        obj = self.TestClass(value=[1, 2, 3])
        objdict = obj._as_runtime()
        self.assertEqual(objdict["class__"], "TestClass")
        self.assertEqual(objdict["data__"]["value"], [1, 2, 3])

    def test_matlabclass_index_processing(self):
        obj = self.TestClass(value=np.arange(10))
        index = obj._process_index(slice(1, 5))
        self.assertTrue(np.array_equal(index, np.array([2, 3, 4, 5])))

    def test_matlabclass_invalid_index(self):
        obj = self.TestClass(value=np.arange(10))
        with self.assertRaises(IndexError):
            obj[15]


if __name__ == "__main__":
    unittest.main()
