from spm.__wrapper__ import Runtime


def mci_rphase_fx(*args, **kwargs):
  """  Flow function for phase model  
    FORMAT [f] = mci_rphase_fx (x,u,P,M)  
     
    x      state vector  
    u      inputs  
    P      parameter vector  
    M      model structure  
     
    f      dx/dt  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/models/phase/mci_rphase_fx.m)
  """

  return Runtime.call("mci_rphase_fx", *args, **kwargs)
