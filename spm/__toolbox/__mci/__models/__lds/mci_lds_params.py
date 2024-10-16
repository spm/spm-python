from spm.__wrapper__ import Runtime


def mci_lds_params(*args, **kwargs):
  """  LDS constrained: sample params from prior  
    FORMAT [P] = mci_lds_params (M,U)  
     
    M     Model structure  
    U     Inputs  
     
    P     Parameters  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/models/lds/mci_lds_params.m)
  """

  return Runtime.call("mci_lds_params", *args, **kwargs)
