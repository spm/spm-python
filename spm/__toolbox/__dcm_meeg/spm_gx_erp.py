from spm._runtime import Runtime


def spm_gx_erp(*args, **kwargs):
    r"""
      Observer for a neural mass model of event related potentials  
        FORMAT [y] = spm_gx_erp(x,u,P,M)  
        x      - state vector  
        y      - measured voltage y = L*x(:)  
       __________________________________________________________________________  
         
        David O, Friston KJ (2003) A neural mass model for MEG/EEG: coupling and  
        neuronal dynamics. NeuroImage 20: 1743-1755  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/dcm_meeg/spm_gx_erp.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_gx_erp", *args, **kwargs)
