from mpython import Runtime


def test_checkcode(*args, **kwargs):
    """
      Test for possible problems in all of MATLAB code files
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/tests/test_checkcode.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("test_checkcode", *args, **kwargs)
