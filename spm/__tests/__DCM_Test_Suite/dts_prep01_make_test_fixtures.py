from spm._runtime import Runtime


def dts_prep01_make_test_fixtures(*args, **kwargs):
    r"""
      Generate immutable DCM M/EEG prep fixtures under SPM tests/data.  
        Authored by Pranay Yadav in 2026  
         
        This is an explicit maintenance script. Runtime tests do not call it.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/tests/DCM_Test_Suite/dts_prep01_make_test_fixtures.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("dts_prep01_make_test_fixtures", *args, **kwargs)
