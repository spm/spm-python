from spm.__wrapper__ import Runtime


def spm_hist(*args, **kwargs):
  """  Generate a weighted histogram - a compiled routine  
    FORMAT h = spm_hist(ind,val)  
    ind - indices (unsigned byte)  
    val - weights  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_hist.m)
  """

  return Runtime.call("spm_hist", *args, **kwargs)
