from spm.__wrapper__ import Runtime


def spm_dcm_fnirs_params(*args, **kwargs):
    """
      Calculate DCM parameters using estimated latent variables  
        FORMAT [A, B, C] = spm_dcm_fnirs_params(DCM)  
         
        DCM  - DCM structure (see spm_dcm_ui)  
         
        A - Endogenous (fixed) connections  
        B - Connections modulated by input  
        C - Influence of input on regional activity   
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_fnirs/spm_dcm_fnirs_params.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_fnirs_params", *args, **kwargs)
