import unittest

from spm import Struct, Cell, Array


class ImplicitTestCase(unittest.TestCase):
    def test_array(self):
        x = Array()
        x[2] = 3
        self.assertListEqual(x.tolist(), [0, 0, 3])

        x = Array()
        x[1:3] = [2, 3]
        self.assertListEqual(x.tolist(), [0, 2, 3])

        self.assertRaises(IndexError, lambda: Array()[2])

    def test_cell(self):
        x = Cell()
        x[2] = 3
        self.assertEqual(x[0].shape, (0, 0))
        self.assertEqual(x[1].shape, (0, 0))
        self.assertEqual(x[2], 3)

        x = Cell()
        x[1:3] = [2, 3]
        self.assertEqual(x[0].shape, (0, 0))
        self.assertListEqual(x[1:3].tolist(), [2, 3])

        self.assertRaises(IndexError, lambda: Cell()[2] * 2)

    def test_struct(self):
        x = Struct()
        x.a = 3
        self.assertEqual(x.a, 3)

        x = Struct()
        x[1] = {"a": 3}
        self.assertTrue(x.shape == (2,))
        self.assertEqual(x[1].a, 3)
        self.assertTrue(x[0].a.shape == (0, 0))

        self.assertRaises(AttributeError, lambda: Struct().a * 2)
        self.assertRaises(KeyError, lambda: Struct()["a"] * 2)
        self.assertRaises(KeyError, lambda: Struct()[1].a * 2)

    def test_cell_of_struct(self):
        x = Cell()
        x(0).a = 1
        self.assertTrue(isinstance(x[0], Struct))
        self.assertEqual(x[0].a, 1)

    def test_struct_of_cell(self):
        x = Struct()
        x.a(0).b = 1
        self.assertTrue(isinstance(x.a, Cell))
        self.assertTrue(isinstance(x.a[0], Struct))
        self.assertEqual(x.a[0].b, 1)

    def test_struct_of_cell_reuse(self):
        x = Struct()
        x.a[0] = "a"
        # This is to make sure that x.a owns its data after the first
        # finalization. If it did not own its data, the resize triggered
        # by a[1] in the following line would raise an error.
        x.a[1] = "b"
