from spm.__wrapper__ import Runtime


def test_regress_spm_opm(*args, **kwargs):
    """
      regresion test for OPM functions  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/tests/test_regress_spm_opm.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("test_regress_spm_opm", *args, **kwargs)
