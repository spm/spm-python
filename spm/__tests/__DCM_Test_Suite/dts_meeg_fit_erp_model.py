from spm._runtime import Runtime


def dts_meeg_fit_erp_model(*args, **kwargs):
    r"""
      Fit one ERP-family DCM model to one staged M/EEG dataset.  
        Authored by Pranay Yadav in 2026  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/tests/DCM_Test_Suite/dts_meeg_fit_erp_model.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("dts_meeg_fit_erp_model", *args, **kwargs)
