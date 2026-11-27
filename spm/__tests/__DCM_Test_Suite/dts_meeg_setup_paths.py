from spm._runtime import Runtime


def dts_meeg_setup_paths(*args, **kwargs):
    r"""
      Add SPM regression suite helper/test paths needed by scripts and tests.  
        Authored by Pranay Yadav in 2026  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/tests/DCM_Test_Suite/dts_meeg_setup_paths.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("dts_meeg_setup_paths", *args, **kwargs)
