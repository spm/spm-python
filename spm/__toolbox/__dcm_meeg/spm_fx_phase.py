from spm.__wrapper__ import Runtime


def spm_fx_phase(*args, **kwargs):
    """
      State equation for a phase-coupled oscillator  
        FORMAT [f,J] = spm_fx_phase (phi,u,P,M)  
         
        phi       state variable  
        u         []  
        P         model (variable) parameter structure  
        M         model (fixed) parameter structure  
         
        f         Flow vector, dphi/dt  
        J         Jacobian, J(i,j)=df_i/dphi_j  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_fx_phase.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_fx_phase", *args, **kwargs)
