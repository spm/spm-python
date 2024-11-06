from spm.__wrapper__ import Runtime


def spm_gx_fmri(*args, **kwargs):
    """
      Simulated BOLD response to input  
        FORMAT [g,dgdx] = spm_gx_fmri(x,u,P,M)  
        g          - BOLD response (%)  
        x          - state vector     (see spm_fx_fmri)  
        P          - Parameter vector (see spm_fx_fmri)  
        M          - model specification structure (see spm_nlsi)  
       __________________________________________________________________________  
         
        This function implements the BOLD signal model described in:   
         
        Stephan KE, Weiskopf N, Drysdale PM, Robinson PA, Friston KJ (2007)  
        Comparing hemodynamic models with DCM. NeuroImage 38: 387-401.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_gx_fmri.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_gx_fmri", *args, **kwargs)
