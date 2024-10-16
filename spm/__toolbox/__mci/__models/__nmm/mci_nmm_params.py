from spm.__wrapper__ import Runtime


def mci_nmm_params(*args, **kwargs):
  """  Generate parameters for two region NMM   
    FORMAT [P] = mci_nmm_params (M,U)  
     
    M         Model structure  
    U         Inputs  
     
    P         Parameters  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/models/nmm/mci_nmm_params.m)
  """

  return Runtime.call("mci_nmm_params", *args, **kwargs)
