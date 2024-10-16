from spm.__wrapper__ import Runtime


def mci_ramsay_gen(*args, **kwargs):
  """  Generate data from Ramsay model  
    FORMAT [Y] = mci_ramsay_gen (P,M,U)  
     
    P         Parameters  
    M         Model structure  
    U         Inputs  
     
    Y         Data  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/models/ramsay/mci_ramsay_gen.m)
  """

  return Runtime.call("mci_ramsay_gen", *args, **kwargs)
