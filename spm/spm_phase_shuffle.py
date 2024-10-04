from spm.__wrap__ import _Runtime


def spm_phase_shuffle(*args, **kwargs):
  """  Phase-shuffling of a vector  
    FORMAT [y] = spm_phase_shuffle(x,[n])  
    x   - data matrix (time-series in columns)  
    n   - optional window length for windowed shuffling  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_phase_shuffle.m)
  """

  return _Runtime.call("spm_phase_shuffle", *args, **kwargs)
