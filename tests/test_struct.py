import unittest
import numpy as np

from spm import Struct


class TestStruct(unittest.TestCase):
    def setUp(self):
        self.struct = Struct(bar='foo')

    def test_set_and_get_attribute(self):
        self.struct.foo = "bar"
        self.assertEqual(self.struct.foo, "bar")
        self.assertEqual(self.struct["foo"], "bar")

        self.assertEqual(self.struct.bar, 'foo')
        self.assertEqual(self.struct['bar'], 'foo')

    def test_set_and_get_item(self):
        self.struct["baz"] = 42
        self.assertEqual(self.struct.baz, 42)
        self.assertEqual(self.struct["baz"], 42)

    def test_delete_item(self):
        self.struct["key"] = "value"
        del self.struct["key"]
        with self.assertRaises(KeyError):
            _ = self.struct["key"]

    def test_as_array(self):
        a = np.asarray(self.struct) 
        b = np.asarray(self.struct, dtype=object) 

if __name__ == "__main__":
    unittest.main()