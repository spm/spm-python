from spm._runtime import Runtime


def dts_meeg_add_eeg_bem_forward(*args, **kwargs):
    r"""
      Build a template EEG BEM forward model and full gain matrix for one M/EEG file.  
        Authored by Pranay Yadav in 2026  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/tests/DCM_Test_Suite/dts_meeg_add_eeg_bem_forward.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("dts_meeg_add_eeg_bem_forward", *args, **kwargs)
