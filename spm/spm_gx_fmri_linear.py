from spm._runtime import Runtime


def spm_gx_fmri_linear(*args, **kwargs):
    r"""
      Simulated BOLD response to input (linear version)  
        FORMAT [y] = spm_gx_fmri_linear(x,u,P,M)  
        y          - BOLD response (%)  
        x          - state vector     (see spm_fx_fmri)  
        P          - Parameter vector (see spm_fx_fmri)  
        M          - model specification structure (see spm_nlsi)  
       __________________________________________________________________________  
         
        This function implements the BOLD signal model described in:   
         
        Stephan KE, Weiskopf N, Drysdale PM, Robinson PA, Friston KJ (2007)  
        Comparing hemodynamic models with DCM. NeuroImage 38: 387-401.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_gx_fmri_linear.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_gx_fmri_linear", *args, **kwargs)
