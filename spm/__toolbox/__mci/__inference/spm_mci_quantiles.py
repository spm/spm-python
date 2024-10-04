from spm.__wrap__ import _Runtime


def spm_mci_quantiles(*args, **kwargs):
  """  Plot histogram and quantiles of posterior density  
    FORMAT [y] = spm_mci_quantiles (post,j,q3,expP)  
     
    post      posterior data structure  
    j         jth variate  
    q3        plot quantiles on histogram  
    expP      exponentiate parameters before plotting ?  
     
    y         2.5%, 50%, 97.5% quantiles  
     
    Solid lines show quantiles from posterior samples  
    Dotted lines under Gaussian assumptions  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/inference/spm_mci_quantiles.m)
  """

  return _Runtime.call("spm_mci_quantiles", *args, **kwargs)
