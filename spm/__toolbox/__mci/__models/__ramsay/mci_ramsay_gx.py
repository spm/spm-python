from spm.__wrapper__ import Runtime


def mci_ramsay_gx(*args, **kwargs):
  """  Observation equation for Ramsay model  
    FORMAT [y,L] = spm_ramsay_gx (x,u,P,M)  
     
    x,u,P,M     state,input,params,model  
     
    y           observations  
    L           dy/dx  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/models/ramsay/mci_ramsay_gx.m)
  """

  return Runtime.call("spm_ramsay_gx", *args, **kwargs)
