from spm.__wrapper__ import Runtime


def spm_fy_erp(*args, **kwargs):
    """
      Feature selection for erp models   
        FORMAT f = spm_fy_erp(y,M)  
        f = y*M.U;  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_fy_erp.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_fy_erp", *args, **kwargs)
