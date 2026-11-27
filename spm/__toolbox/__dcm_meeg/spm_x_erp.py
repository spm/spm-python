from spm._runtime import Runtime


def spm_x_erp(*args, **kwargs):
    r"""
      Initial state of a neural mass model of erps  
        FORMAT [x] = spm_x_erp(P)  
        P - parameters  
         
        x        - x(0)  
       __________________________________________________________________________  
        David O, Friston KJ (2003) A neural mass model for MEG/EEG: coupling and  
        neuronal dynamics. NeuroImage 20: 1743-1755  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/dcm_meeg/spm_x_erp.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_x_erp", *args, **kwargs)
