from spm._runtime import Runtime


def spm_gx_state_fnirs(*args, **kwargs):
    r"""
      Neurodynamics and Hemodynamics underling DCM for fNIRS  
        FORMAT [y] = spm_gx_state_fnirs(x,u,P,M)  
         
        x   - state vector     (see spm_fx_fnirs)  
        u   - experimental inputs   
        P   - prior of latent variables   
        M   - model structure  
         
        y   - fNIRS response and copied state vector  
         
        The `copied state vector' passes the first hidden variable in each region  
        to the output variable y, so that neuronal activity and state variables  
        can be plotted.   
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/dcm_fnirs/spm_gx_state_fnirs.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_gx_state_fnirs", *args, **kwargs)
