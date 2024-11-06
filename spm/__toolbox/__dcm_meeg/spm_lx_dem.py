from spm.__wrapper__ import Runtime


def spm_lx_dem(*args, **kwargs):
    """
      Observer matrix for a neural mass model of erps: y = G*x  
        FORMAT [G] = spm_lx_dem(P,M)  
        x      - state vector  
        G      - where y = G*x; G = L*J  
                 L = dy/dsource  
                 J = dsource/dstate  
       __________________________________________________________________________  
         
        David O, Friston KJ (2003) A neural mass model for MEG/EEG: coupling and  
        neuronal dynamics. NeuroImage 20: 1743-1755  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_lx_dem.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_lx_dem", *args, **kwargs)
