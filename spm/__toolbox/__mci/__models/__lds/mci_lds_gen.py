from spm.__wrap__ import _Runtime


def mci_lds_gen(*args, **kwargs):
  """  LDS constrained: generate data  
    FORMAT [Y] = mci_lds_gen (M,U,P)  
     
    M     Model structure  
    U     Inputs  
    P     Parameters  
     
    Y     Data  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/models/lds/mci_lds_gen.m)
  """

  return _Runtime.call("mci_lds_gen", *args, **kwargs)
