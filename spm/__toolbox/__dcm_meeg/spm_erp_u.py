from spm.__wrapper__ import Runtime


def spm_erp_u(*args, **kwargs):
    """
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_erp_u.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_erp_u", *args, **kwargs)
