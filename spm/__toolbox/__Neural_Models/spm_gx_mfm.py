from spm.__wrap__ import _Runtime


def spm_gx_mfm(*args, **kwargs):
  """  observer for a mean-field model (spiking)  
    FORMAT [m] = spm_gx_mfm(x,u,P,M)  
    x      - state vector  
    m      - spiking activity (ns x np)  
   __________________________________________________________________________  
     
    David O, Friston KJ (2003) A neural mass model for MEG/EEG: coupling and  
    neuronal dynamics. NeuroImage 20: 1743-1755  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/Neural_Models/spm_gx_mfm.m)
  """

  return _Runtime.call("spm_gx_mfm", *args, **kwargs)
