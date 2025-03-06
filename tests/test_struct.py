import unittest
import numpy as np

from spm import Struct, Array


class TestStruct(unittest.TestCase):
    def setUp(self):
        self.struct = Struct()

    def test_set_and_get_attribute(self):
        self.struct.foo = "bar"
        self.assertEqual(self.struct.foo, "bar")
        self.assertEqual(self.struct["foo"], "bar")
        self.assertListEqual(list(self.struct.keys()), ["foo"])
        self.assertListEqual(list(self.struct.values()), ["bar"])
        self.assertListEqual(list(self.struct.items()), [("foo", "bar")])

        self.struct.bar = "foo"
        self.assertEqual(self.struct.bar, 'foo')
        self.assertEqual(self.struct['bar'], 'foo')
        self.assertListEqual(list(self.struct.keys()), ["foo", "bar"])
        self.assertListEqual(list(self.struct.values()), ["bar", "foo"])
        self.assertListEqual(list(self.struct.items()),
                             [("foo", "bar"), ("bar", "foo")])

    def test_set_and_get_item(self):
        self.struct["baz"] = 42
        self.assertEqual(self.struct.baz, 42)
        self.assertEqual(self.struct["baz"], 42)

    def test_delete_item(self):
        self.struct["key"] = "value"
        self.assertTrue("key" in self.struct.keys())
        del self.struct["key"]
        self.assertTrue("key" not in self.struct.keys())

    def test_as_array(self):
        self.struct.foo = "bar"
        a = np.asarray(self.struct)
        self.assertEqual(a.item(), dict(self.struct))
        a = np.asarray(self.struct, dtype=object)
        self.assertEqual(a.item(), dict(self.struct))

    def test_struct_as_array_after_initialization(self):
        self.struct.foo = "bar"
        self.struct.bar = "baz"
        self.struct[1].baz = 42 

        keys = set(('foo', 'bar', 'baz'))

        # All fields exist in struct array
        self.assertSetEqual(keys, set(self.struct.keys()))

        # All fields exist in first slice
        self.assertSetEqual(keys, set(self.struct[0].keys()))

        # All fields exist in second slice
        self.assertSetEqual(keys, set(self.struct[1].keys()))

        # Specified elements are correct
        self.assertEqual(self.struct[0].foo, "bar")
        self.assertEqual(self.struct[0].bar, "baz")
        self.assertEqual(self.struct[1].baz, 42)

        # Unspecified elements are empty arrays
        self.assertIsInstance(self.struct[0].baz, Array)
        self.assertTupleEqual(self.struct[0].baz.shape, tuple())
        self.assertIsInstance(self.struct[1].foo, Array)
        self.assertTupleEqual(self.struct[1].foo.shape, tuple())
        self.assertIsInstance(self.struct[1].bar, Array)
        self.assertTupleEqual(self.struct[1].bar.shape, tuple())

if __name__ == "__main__":
    unittest.main()
