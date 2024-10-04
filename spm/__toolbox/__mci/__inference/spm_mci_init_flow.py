from spm.__wrap__ import _Runtime


def spm_mci_init_flow(*args, **kwargs):
  """  Extract init, flow and out params from rfx and ffx vectors  
    FORMAT [x_init,x_flow] = spm_mci_init_flow (assign,w,v,M)  
     
    assign    fields specify which are random/fixed effects  
    w         random effects vector  
    v         fixed effects vector  
    M         model structure  
     
    x_init    init params  
    x_flow    flow params (includes out params)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/inference/spm_mci_init_flow.m)
  """

  return _Runtime.call("spm_mci_init_flow", *args, **kwargs)
