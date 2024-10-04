from spm.__wrap__ import _Runtime


def mci_nmm_gen(*args, **kwargs):
  """  Generate data from two region NMM   
    FORMAT [Y] = mci_nmm_gen (M,U,P)  
     
    M         Model structure  
    U         Inputs  
    P         Parameters  
     
    Y         Data  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/models/nmm/mci_nmm_gen.m)
  """

  return _Runtime.call("mci_nmm_gen", *args, **kwargs)
