from mpython import Runtime


def test_spm_cat_struct(*args, **kwargs):
    """
      Unit Tests for spm_cat_struct
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/tests/test_spm_cat_struct.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("test_spm_cat_struct", *args, **kwargs)
