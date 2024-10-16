from spm.__wrapper__ import Runtime


def _timelock2freq(*args, **kwargs):
  """  TIMELOCK2FREQ transform the reconstructed dipole moment into  
    something that again resembles the physical input parameter in  
    the frequency domain.   
     
    This is needed after source reconstruction using FREQ2TIMELOCK.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/timelock2freq.m)
  """

  return Runtime.call("timelock2freq", *args, **kwargs)
