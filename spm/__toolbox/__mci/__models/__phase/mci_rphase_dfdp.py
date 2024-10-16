from spm.__wrapper__ import Runtime


def mci_rphase_dfdp(*args, **kwargs):
  """  Parameter sensitivity for phase model  
    FORMAT [dfdp] = mci_rphase_dfdp (x,u,P,M)  
     
    x      State vector  
    u      inputs  
    P      parameter vector  
    M      model structure  
     
    dfdp   Jacobian wrt. parameters, df/dp  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/models/phase/mci_rphase_dfdp.m)
  """

  return Runtime.call("mci_rphase_dfdp", *args, **kwargs)
