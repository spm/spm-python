from spm.__wrapper__ import Runtime


def spm_dcm_fnirs_params(*args, **kwargs):
  """  Calculate DCM parameters using estimated latent variables  
    FORMAT [A, B, C] = spm_dcm_fnirs_params(DCM)  
     
    DCM  - DCM structure (see spm_dcm_ui)  
     
    A - Endogenous (fixed) connections  
    B - Connections modulated by input  
    C - Influence of input on regional activity   
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/dcm_fnirs/spm_dcm_fnirs_params.m)
  """

  return Runtime.call("spm_dcm_fnirs_params", *args, **kwargs)
