from spm.__wrapper__ import Runtime


def spm_gx_mfm(*args, **kwargs):
    """
      observer for a mean-field model (spiking)  
        FORMAT [m] = spm_gx_mfm(x,u,P,M)  
        x      - state vector  
        m      - spiking activity (ns x np)  
       __________________________________________________________________________  
         
        David O, Friston KJ (2003) A neural mass model for MEG/EEG: coupling and  
        neuronal dynamics. NeuroImage 20: 1743-1755  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Neural_Models/spm_gx_mfm.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_gx_mfm", *args, **kwargs)
