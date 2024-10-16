from spm.__wrapper__ import Runtime


def mci_rphase_gen(*args, **kwargs):
  """  Generate data from reduced WCO model  
    FORMAT [Y] = mci_rphase_gen (P,M,U)  
     
    P     parameters  
    M     model structure  
    U     inputs  
     
    Y     data  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/models/phase/mci_rphase_gen.m)
  """

  return Runtime.call("mci_rphase_gen", *args, **kwargs)
