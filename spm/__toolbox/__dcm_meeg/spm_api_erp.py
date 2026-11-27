from spm._runtime import Runtime


def spm_api_erp(*args, **kwargs):
    r"""
      SPM_API_ERP Application M-file for spm_api_erp.fig  
           FIG = SPM_API_ERP launch spm_api_erp GUI.  
           SPM_API_ERP('callback_name', ...) invoke the named callback.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/dcm_meeg/spm_api_erp.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_api_erp", *args, **kwargs)
