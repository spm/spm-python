from spm.__wrapper__ import Runtime


def mci_ramsay_struct(*args, **kwargs):
  """  Data structures for Ramsay model  
    FORMAT [M,U] = mci_ramsay_struct (sigme_e)  
     
    sigma_e       Noise SD  
     
    M,U           model, input data structures  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/models/ramsay/mci_ramsay_struct.m)
  """

  return Runtime.call("mci_ramsay_struct", *args, **kwargs)
