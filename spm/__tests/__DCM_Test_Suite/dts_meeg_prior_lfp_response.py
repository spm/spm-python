from spm._runtime import Runtime


def dts_meeg_prior_lfp_response(*args, **kwargs):
    r"""
      Generate the default-prior one-node LFP response used by simulated tests.  
        Authored by Pranay Yadav in 2026  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/tests/DCM_Test_Suite/dts_meeg_prior_lfp_response.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("dts_meeg_prior_lfp_response", *args, **kwargs)
