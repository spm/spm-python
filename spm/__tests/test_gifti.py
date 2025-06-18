from mpython import Runtime


def test_gifti(*args, **kwargs):
    """
      Unit Tests for gifti
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/tests/test_gifti.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("test_gifti", *args, **kwargs)
