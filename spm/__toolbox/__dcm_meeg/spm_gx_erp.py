from spm.__wrapper__ import Runtime


def spm_gx_erp(*args, **kwargs):
    """
      Observer for a neural mass model of event related potentials  
        FORMAT [y] = spm_gx_erp(x,u,P,M)  
        x      - state vector  
        y      - measured voltage y = L*x(:)  
       __________________________________________________________________________  
         
        David O, Friston KJ (2003) A neural mass model for MEG/EEG: coupling and  
        neuronal dynamics. NeuroImage 20: 1743-1755  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_gx_erp.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_gx_erp", *args, **kwargs)
