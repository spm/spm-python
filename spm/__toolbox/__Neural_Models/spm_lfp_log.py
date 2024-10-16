from spm.__wrapper__ import Runtime


def spm_lfp_log(*args, **kwargs):
  """  Feature selection for lfp and mtf (spectral) neural mass models  
    FORMAT [y] = spm_lfp_log(y,M)  
      
    Y -> log(y) (including cells)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/Neural_Models/spm_lfp_log.m)
  """

  return Runtime.call("spm_lfp_log", *args, **kwargs)
