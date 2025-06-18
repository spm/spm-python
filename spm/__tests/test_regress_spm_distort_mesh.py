from mpython import Runtime


def test_regress_spm_distort_mesh(*args, **kwargs):
    """
    test_regress_spm_distort_mesh is a function.
          tests = test_regress_spm_distort_mesh(TestCase)


    [Matlab code]( https://github.com/spm/spm/blob/main/tests/test_regress_spm_distort_mesh.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("test_regress_spm_distort_mesh", *args, **kwargs)
