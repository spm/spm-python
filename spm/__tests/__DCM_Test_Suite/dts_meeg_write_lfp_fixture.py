from spm._runtime import Runtime


def dts_meeg_write_lfp_fixture(*args, **kwargs):
    r"""
      Write a one-channel LFP waveform as an SPM M/EEG object.  
        Authored by Pranay Yadav in 2026  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/tests/DCM_Test_Suite/dts_meeg_write_lfp_fixture.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("dts_meeg_write_lfp_fixture", *args, **kwargs)
