from spm._runtime import Runtime


def spm_fy_erp(*args, **kwargs):
    r"""
      Feature selection for erp models   
        FORMAT f = spm_fy_erp(y,M)  
        f = y*M.U;  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/dcm_meeg/spm_fy_erp.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_fy_erp", *args, **kwargs)
