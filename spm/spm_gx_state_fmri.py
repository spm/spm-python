from spm.__wrapper__ import Runtime


def spm_gx_state_fmri(*args, **kwargs):
    """
      Simulated BOLD response and copied state vector  
        FORMAT [y] = spm_gx_state_fmri(x,u,P,M)  
        y          - BOLD response and copied state vector  
         
        x          - state vector     (see spm_fx_fmri)  
        P          - Parameter vector (see spm_fx_fmri)  
        M          - model specification structure (see spm_nlsi)  
         
        The `copied state vector' passes the first hidden variable in each region  
        to the output variable y, so that 'neural activities' can be plotted   
        by spm_dcm_generate.m  
         
        See spm_fx_fmri.m and spm_dcm_generate.m  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_gx_state_fmri.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_gx_state_fmri", *args, **kwargs)
