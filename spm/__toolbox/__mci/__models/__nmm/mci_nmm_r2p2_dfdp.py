from spm.__wrapper__ import Runtime


def mci_nmm_r2p2_dfdp(*args, **kwargs):
  """  Parameter Jacobian for two region, two parameter NMM  
    FORMAT [F] = mci_nmm_r2p2_dfdp (x,u,P,M)  
     
    x         State  
    u         Inputs  
    P         Parameters  
    M         Model structure  
     
    F         F(i,j) = df(x)_i/dp_j  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/models/nmm/mci_nmm_r2p2_dfdp.m)
  """

  return Runtime.call("mci_nmm_r2p2_dfdp", *args, **kwargs)
