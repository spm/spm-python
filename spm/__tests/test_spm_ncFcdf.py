from mpython import Runtime


def test_spm_ncFcdf(*args, **kwargs):
    """
      Unit Tests for spm_ncFcdf
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/tests/test_spm_ncFcdf.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("test_spm_ncFcdf", *args, **kwargs)
