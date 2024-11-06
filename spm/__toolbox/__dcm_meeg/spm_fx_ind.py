from spm.__wrapper__ import Runtime


def spm_fx_ind(*args, **kwargs):
    """
      State equations for a neural mass model of erps  
        FORMAT [f,J] = spm_fx_erp(x,u,P,M)  
          x(i,j) - power in the i-th region and j-th frequency mode  
         
        f        - dx(t)/dt  = f(x(t))  
        J        - df(t)/dx(t)  
       __________________________________________________________________________  
        David O, Friston KJ (2003) A neural mass model for MEG/EEG: coupling and  
        neuronal dynamics. NeuroImage 20: 1743-1755  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_fx_ind.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_fx_ind", *args, **kwargs)
