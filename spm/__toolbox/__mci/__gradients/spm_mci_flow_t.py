from spm.__wrapper__ import Runtime


def spm_mci_flow_t(*args, **kwargs):
  """  Evaluate flow at time t  
    FORMAT [dxdt] = spm_mci_flow_t (t,x,U,P,M)  
     
    t     time  
    x     state  
    U     inputs  
    P     parameters  
    M     model  
     
    dxdt  flow, dx/dt  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/gradients/spm_mci_flow_t.m)
  """

  return Runtime.call("spm_mci_flow_t", *args, **kwargs)
