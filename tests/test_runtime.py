import unittest


class TestRuntime(unittest.TestCase):
    def test_import_package(self):
        try:
            pass
        except Exception:
            self.fail("Cannot import package.")

    def test_import_runtime(self):
        try:
            pass
        except Exception:
            self.fail("Cannot import Runtime.")

    def test_initialise_runtime(self):
        try:
            from spm import Runtime

            Runtime.instance()
        except Exception:
            self.fail("Cannot initialise Runtime.")

    def test_call_matlab(self):
        result = None
        try:
            from spm import Runtime

            result = Runtime.call("eval", "1+1")
        except Exception:
            self.fail("Calling Matlab failed.")

        self.assertEqual(result, 2)

    def test_call_matlab_noargout(self):
        result = True
        try:
            from spm import Runtime

            result = Runtime.call("magic", 0, nargout=0)
        except Exception:
            self.fail("Calling Matlab without argout failed.")

        self.assertTrue(result is None)

    def test_0d_empty_cell_to_matlab(self):
        try:
            from spm import Runtime, Cell

            idt = Runtime.call("eval", "@(x) x")
            c = Cell()
            c2 = idt(c)
        except Exception:
            self.fail("OD empty cell to Matlab failed.")

        self.assertIsInstance(c2, Cell)
        self.assertEqual(c2.shape, c.shape)

    def test_1d_empty_cell_to_matlab(self):
        try:
            from spm import Runtime, Cell

            idt = Runtime.call("eval", "@(x) x")
            c = Cell(3)
            c2 = idt(c)
        except Exception:
            self.fail("1D empty cell to Matlab failed.")

        self.assertIsInstance(c2, Cell)
        self.assertEqual(c2.shape, c.shape)

    def test_2d_empty_cell_to_matlab(self):
        try:
            from spm import Runtime, Cell

            idt = Runtime.call("eval", "@(x) x")
            c = Cell(3, 2)
            c2 = idt(c)
        except Exception:
            self.fail("2D empty cell to Matlab failed.")

        self.assertIsInstance(c2, Cell)
        self.assertEqual(c2.shape, c.shape)

    def test_1d_cell_to_matlab(self):
        try:
            from spm import Runtime, Cell

            idt = Runtime.call("eval", "@(x) x")
            c = Cell.from_any([1, 2, 3])
            c2 = idt(c)
        except Exception:
            self.fail("1D cell to Matlab failed.")

        self.assertIsInstance(c2, Cell)
        self.assertEqual(c2.shape, c.shape)
        self.assertTrue(c2.tolist() == c.tolist())

    def test_2d_cell_to_matlab(self):
        try:
            from spm import Runtime, Cell
            import numpy as np

            idt = Runtime.call("eval", "@(x) x")
            c = Cell.from_array(np.random.randn(2, 3))
            c2 = idt(c)
        except Exception:
            self.fail("1D cell to Matlab failed.")

        self.assertIsInstance(c2, Cell)
        self.assertEqual(c2.shape, c.shape)
        self.assertTrue(c2.tolist() == c.tolist())

    def test_empty_struct_to_matlab(self):
        try:
            from spm import Runtime, Struct

            idt = Runtime.call("eval", "@(x) x")
            s = Struct()
            s2 = idt(s)
        except Exception:
            self.fail("Empty struct to Matlab failed.")

        self.assertIsInstance(s2, Struct)
        self.assertEqual(s2.shape, s.shape)

    def test_empty_array_to_matlab(self):
        try:
            from spm import Runtime, Array

            idt = Runtime.call("eval", "@(x) x")
            a = Array()
            a2 = idt(a)
        except Exception:
            self.fail("Empty array to Matlab failed.")

        self.assertIsInstance(a2, Array)
        self.assertEqual(a2.shape, a.shape)


if __name__ == "__main__":
    unittest.main()
