import unittest
import numpy as np
from itertools import product

from spm import Struct, Array, Runtime


class TestStruct(unittest.TestCase):
    def setUp(self):
        self.struct = Struct()

    def test_struct_instantiate_empty(self):
        # Construct an empty struct
        s = Struct()

        # Check proper construction
        self.assertIsInstance(s, Struct)
        self.assertEqual(len(s), 0)

    def test_struct_instantiate_empty_1d(self):
        # Construct a 1x3 struct array
        s = Struct(3)

        # Check proper construction
        self.assertIsInstance(s, Struct)
        self.assertTupleEqual(s.shape, (3,))
        self.assertEqual(s.size, 3)
        self.assertTrue(all(isinstance(s[i], Struct) for i in range(3)))

    def test_struct_instantiate_empty_2d_row(self):
        # Construct a 1x3 struct array
        s = Struct(1, 3)

        # Check proper construction
        self.assertIsInstance(s, Struct)
        self.assertTupleEqual(s.shape, (1, 3))
        self.assertEqual(s.size, 3)
        self.assertTrue(all(isinstance(s[0, i], Struct) for i in range(3)))

    def test_struct_instantiate_empty_2d_col(self):
        # Construct a 3x1 struct array
        s = Struct(3, 1)

        # Check proper construction
        self.assertIsInstance(s, Struct)
        self.assertTupleEqual(s.shape, (3, 1))
        self.assertEqual(s.size, 3)
        self.assertTrue(all(isinstance(s[i, 0], Struct) for i in range(3)))

    def test_struct_instantiate_empty_2d(self):
        # Construct a 3x2 struct array
        s = Struct(3, 2)

        # Check proper construction
        self.assertIsInstance(s, Struct)
        self.assertTupleEqual(s.shape, (3, 2))

        self.assertTrue(
            all(isinstance(s[i, j], Struct) for i, j in product(range(3), range(2)))
        )

    def test_struct_instantiate_empty_nd(self):
        # Construct a 2x3x4x5 struct array
        s = Struct(2, 3, 4, 5)

        # Check proper construction
        self.assertIsInstance(s, Struct)
        self.assertTupleEqual(s.shape, (2, 3, 4, 5))

        self.assertTrue(
            all(
                isinstance(s[i, j, k, m], Struct)
                for i, j, k, m in product(range(2), range(3), range(4), range(5))
            )
        )

    def test_struct_set_and_get_attribute(self):
        self.struct.foo = "bar"
        self.assertEqual(self.struct.foo, "bar")
        self.assertEqual(self.struct["foo"], "bar")
        self.assertListEqual(list(self.struct.keys()), ["foo"])
        self.assertListEqual(list(self.struct.values()), ["bar"])
        self.assertListEqual(list(self.struct.items()), [("foo", "bar")])

        self.struct.bar = "foo"
        self.assertEqual(self.struct.bar, "foo")
        self.assertEqual(self.struct["bar"], "foo")
        self.assertListEqual(list(self.struct.keys()), ["foo", "bar"])
        self.assertListEqual(list(self.struct.values()), ["bar", "foo"])
        self.assertListEqual(
            list(self.struct.items()), [("foo", "bar"), ("bar", "foo")]
        )

    def test_struct_set_and_get_item(self):
        self.struct["baz"] = 42
        self.assertEqual(self.struct.baz, 42)
        self.assertEqual(self.struct["baz"], 42)

    def test_struct_delete_item(self):
        self.struct["key"] = "value"
        self.assertTrue("key" in self.struct.keys())
        del self.struct["key"]
        self.assertTrue("key" not in self.struct.keys())

    def test_struct_as_array(self):
        self.struct.foo = "bar"
        a = np.asarray(self.struct)
        self.assertEqual(a.item(), dict(self.struct))
        a = np.asarray(self.struct, dtype=object)
        self.assertEqual(a.item(), dict(self.struct))

    def test_struct_as_array_after_initialization(self):
        self.struct.foo = "bar"
        self.struct.bar = "baz"
        self.struct[1].baz = 42
        # raise ValueError(self.struct)

        keys = set(("foo", "bar", "baz"))

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
        self.assertTupleEqual(self.struct[0].baz.shape, (0, 0))
        self.assertIsInstance(self.struct[1].foo, Array)
        self.assertTupleEqual(self.struct[1].foo.shape, (0, 0))
        self.assertIsInstance(self.struct[1].bar, Array)
        self.assertTupleEqual(self.struct[1].bar.shape, (0, 0))

    def test_struct_from_matlab(self):
        # Construct a struct in Matlab
        try:
            s_matlab = Runtime.call("eval", "struct('field1', 1, 'field2', 2)")
        except Exception:
            self.fail("Struct from Matlab failed.")

        # Check Runtime conversion
        self.assertIsInstance(s_matlab, Struct)
        self.assertEqual(s_matlab.field1, 1)
        self.assertEqual(s_matlab.field2, 2)
        self.assertListEqual(list(s_matlab.keys()), ["field1", "field2"])
        self.assertListEqual(list(s_matlab.values()), [1, 2])
        self.assertListEqual(list(s_matlab.items()), [("field1", 1), ("field2", 2)])

    def test_struct_from_matlab_nested(self):
        # Construct a nested struct in Matlab
        try:
            s_matlab = Runtime.call(
                "eval", "struct('field1', struct('subfield1', 1), 'field2', 2)"
            )
        except Exception:
            self.fail("Nested struct from Matlab failed.")

        # Check Runtime conversion
        self.assertIsInstance(s_matlab, Struct)
        self.assertIsInstance(s_matlab.field1, Struct)
        self.assertEqual(s_matlab.field1.subfield1, 1)
        self.assertEqual(s_matlab.field2, 2)
        self.assertListEqual(list(s_matlab.keys()), ["field1", "field2"])
        self.assertListEqual(list(s_matlab.field1.keys()), ["subfield1"])
        self.assertListEqual(list(s_matlab.values()), [s_matlab.field1, 2])
        self.assertListEqual(
            list(s_matlab.items()), [("field1", s_matlab.field1), ("field2", 2)]
        )

    def test_struct_from_matlab_with_array(self):
        # Construct a struct with an array in Matlab
        try:
            s_matlab = Runtime.call("eval", "struct('field1', [1, 2, 3], 'field2', 2)")
        except Exception:
            self.fail("Struct with array from Matlab failed.")

        # Check Runtime conversion
        self.assertIsInstance(s_matlab, Struct)
        self.assertIsInstance(s_matlab.field1, Array)
        self.assertListEqual(s_matlab.field1.tolist(), [1, 2, 3])
        self.assertEqual(s_matlab.field2, 2)
        self.assertListEqual(list(s_matlab.keys()), ["field1", "field2"])
        self.assertListEqual(list(s_matlab.values()), [s_matlab.field1, 2])
        self.assertListEqual(
            list(s_matlab.items()), [("field1", s_matlab.field1), ("field2", 2)]
        )

    def test_struct_from_matlab_with_structure_array(self):
        # Construct a struct array of size 2 in Matlab
        try:
            s_matlab = Runtime.call(
                "eval", "repmat(struct('field1', 1, 'field2', 2), 2, 1)"
            )
        except Exception:
            self.fail("Struct array from Matlab failed.")

        # Check Runtime conversion
        self.assertIsInstance(s_matlab, Struct)
        self.assertEqual(len(s_matlab), 2)
        self.assertIsInstance(s_matlab[0, 0], Struct)
        self.assertEqual(s_matlab[0, 0].field1, 1)
        self.assertEqual(s_matlab[0, 0].field2, 2)
        self.assertListEqual(list(s_matlab[0, 0].keys()), ["field1", "field2"])
        self.assertListEqual(list(s_matlab[0, 0].values()), [1, 2])
        self.assertListEqual(
            list(s_matlab[0, 0].items()), [("field1", 1), ("field2", 2)]
        )

        self.assertIsInstance(s_matlab[1, 0], Struct)
        self.assertEqual(s_matlab[1, 0].field1, 1)
        self.assertEqual(s_matlab[1, 0].field2, 2)
        self.assertListEqual(list(s_matlab[1, 0].keys()), ["field1", "field2"])
        self.assertListEqual(list(s_matlab[1, 0].values()), [1, 2])
        self.assertListEqual(
            list(s_matlab[1, 0].items()), [("field1", 1), ("field2", 2)]
        )

    def test_struct_to_matlab_empty(self):
        # Construct an empty struct
        s = Struct()

        # Get properties in Matlab
        try:
            size = Runtime.call("size", s)
            type = Runtime.call("class", s)
            fieldnames = Runtime.call("fieldnames", s)
        except Exception:
            self.fail("Empty struct to Matlab failed.")

        # Check properties in Matlab
        self.assertEqual(size.tolist(), [1, 1])
        self.assertEqual(type, "struct")
        self.assertListEqual(fieldnames.tolist(), [])

    def test_struct_to_matlab_empty_1d(self):
        # Construct a 1x3 struct array
        s = Struct(3)

        # Get properties in Matlab
        try:
            size = Runtime.call("size", s)
            type = Runtime.call("class", s)
            fieldnames = Runtime.call("fieldnames", s)
        except Exception:
            self.fail("1D shape struct to Matlab failed.")

        # Check properties in Matlab
        self.assertEqual(size.tolist(), [1, 3])
        self.assertEqual(type, "struct")
        self.assertListEqual(fieldnames.tolist(), [])

    def test_struct_to_matlab_empty_2d_row(self):
        # Construct a 1x3 struct array
        s = Struct(1, 3)

        # Get properties in Matlab
        try:
            size = Runtime.call("size", s)
            type = Runtime.call("class", s)
            fieldnames = Runtime.call("fieldnames", s)
        except Exception:
            self.fail("1D row struct to Matlab failed.")

        # Check properties in Matlab
        self.assertEqual(size.tolist(), [1, 3])
        self.assertEqual(type, "struct")
        self.assertListEqual(fieldnames.tolist(), [])

    def test_struct_to_matlab_empty_2d_col(self):
        # Construct a 3x1 struct array
        s = Struct(3, 1)

        # Get properties in Matlab
        try:
            size = Runtime.call("size", s)
            type = Runtime.call("class", s)
            fieldnames = Runtime.call("fieldnames", s)
        except Exception:
            self.fail("1D col struct to Matlab failed.")

        # Check properties in Matlab
        self.assertEqual(size.tolist(), [3, 1])
        self.assertEqual(type, "struct")
        self.assertListEqual(fieldnames.tolist(), [])

    def test_struct_to_matlab_empty_2d(self):
        # Construct a 3x2 struct array
        s = Struct(3, 2)

        # Get properties in Matlab
        try:
            size = Runtime.call("size", s)
            type = Runtime.call("class", s)
            fieldnames = Runtime.call("fieldnames", s)
        except Exception:
            self.fail("2D struct to Matlab failed.")

        # Check properties in Matlab
        self.assertEqual(size.tolist(), [3, 2])
        self.assertEqual(type, "struct")
        self.assertListEqual(fieldnames.tolist(), [])


if __name__ == "__main__":
    unittest.main()
