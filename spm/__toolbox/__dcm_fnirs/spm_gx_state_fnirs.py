from spm.__wrapper__ import Runtime


def spm_gx_state_fnirs(*args, **kwargs):
    """
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_fnirs/spm_gx_state_fnirs.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_gx_state_fnirs", *args, **kwargs)
