from spm.__wrapper__ import Runtime


def test_regress_fmri_group(*args, **kwargs):
    """
      Regression tests for second-level SPM for fMRI  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/tests/test_regress_fmri_group.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("test_regress_fmri_group", *args, **kwargs)
