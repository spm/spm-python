from spm._runtime import Runtime


def spm_gx_mfm(*args, **kwargs):
    r"""
      observer for a mean-field model (spiking)  
        FORMAT [m] = spm_gx_mfm(x,u,P,M)  
        x      - state vector  
        m      - spiking activity (ns x np)  
       __________________________________________________________________________  
         
        David O, Friston KJ (2003) A neural mass model for MEG/EEG: coupling and  
        neuronal dynamics. NeuroImage 20: 1743-1755  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/Neural_Models/spm_gx_mfm.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_gx_mfm", *args, **kwargs)
