from spm._runtime import Runtime


def spm_erp_u(*args, **kwargs):
    r"""
      [scalar] input for EEG models (Gaussian function)  
        FORMAT [u] = spm_erp_u(t,P,M)  
        t      - PST (seconds)  
        P      - parameter structure  
          P.R  - scaling of [Gaussian] parameters  
         
        u   - stimulus-related (subcortical) input  
         
        See spm_fx_erp.m and spm_erp_priors.m  
       __________________________________________________________________________  
         
        David O, Friston KJ (2003) A neural mass model for MEG/EEG: coupling and  
        neuronal dynamics. NeuroImage 20: 1743-1755  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/dcm_meeg/spm_erp_u.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_erp_u", *args, **kwargs)
