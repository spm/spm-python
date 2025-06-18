from mpython import Runtime


def test_regress_spm_opm(*args, **kwargs):
    """
      regresion test for OPM functions
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/tests/test_regress_spm_opm.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("test_regress_spm_opm", *args, **kwargs)
