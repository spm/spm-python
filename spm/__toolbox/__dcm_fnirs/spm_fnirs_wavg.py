from spm.__wrapper__ import Runtime


def spm_fnirs_wavg(*args, **kwargs):
  """  Average data across trials   
    FORMAT wy = spm_fnirs_wavg(y,ons,dur)  
     
    y    - data (eg, optical density changes)   
    ons  - onset of average window (eg, onset of tasks)  
    dur  - window size   
     
    wy   - time series averaged across trials  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/dcm_fnirs/spm_fnirs_wavg.m)
  """

  return Runtime.call("spm_fnirs_wavg", *args, **kwargs)
