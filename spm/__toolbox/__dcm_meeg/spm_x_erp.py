from spm.__wrapper__ import Runtime


def spm_x_erp(*args, **kwargs):
    """
      Initial state of a neural mass model of erps  
        FORMAT [x] = spm_x_erp(P)  
        P - parameters  
         
        x        - x(0)  
       __________________________________________________________________________  
        David O, Friston KJ (2003) A neural mass model for MEG/EEG: coupling and  
        neuronal dynamics. NeuroImage 20: 1743-1755  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_x_erp.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_x_erp", *args, **kwargs)
