from spm.__wrapper__ import Runtime


def spm_fx_tfm(*args, **kwargs):
    """
      state equations - time-frequency model with state-dependent parameters  
        FORMAT [f,J,D] = spm_fx_tfm(x,u,P,M)  
        x      - hidden states  
        u      - exogenous input  
         
        f        - dx(t)/dt  = f(x(t))  
        J        - df(t)/dx(t)  
        D        - delay operator dx(t)/dt = f(x(t - d))  
                                           = D(d)*f(x(t))  
         
        This routine is essentially a rapper for the equations of motion  
        specified in M.h - it updates the input dependent parameters and then  
        calls the appropriate equations of motion in the usual way.  
         
       __________________________________________________________________________  
        David O, Friston KJ (2003) A neural mass model for MEG/EEG: coupling and  
        neuronal dynamics. NeuroImage 20: 1743-1755  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_fx_tfm.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_fx_tfm", *args, **kwargs)
