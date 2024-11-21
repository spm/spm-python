import unittest


class TestRuntime(unittest.TestCase):

    def test_import_package(self):
        try:
            import spm
        except: 
            self.fail('Cannot import package.')

    def test_import_runtime(self):
        try:
            from spm import Runtime
        except: 
            self.fail('Cannot import Runtime.')

    def test_initialise_runtime(self):
        try:
            from spm import Runtime
            instance = Runtime.instance()
        except:
            self.fail('Cannot initialise Runtime.')

    def test_call_matlab(self):
        result = None
        try: 
            from spm import Runtime
            result = Runtime.call('eval', '1+1')
        except:
            self.fail('Calling Matlab failed.')

        self.assertEqual(result, 2); 

    def test_call_matlab_noargout(self):
        result = True
        try: 
            from spm import Runtime
            result = Runtime.call('disp', '"test"', nargout=0)
        except:
            self.fail('Calling Matlab without argout failed.')

        self.assertTrue(result is None)



if __name__ == '__main__':
    unittest.main()