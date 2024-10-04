from spm.__wrap__ import _Runtime


def spm_nvc_gen(*args, **kwargs):
  """  Generate a BOLD signal prediction from scaled summed of neuronal drives   
    (neurovascular coupling).  
    FORMAT [y] = spm_nvc_gen(P,M,U)  
     
    Inputs:  
    -------------------------------------------------------------------------  
     P - parameters of neurovascular coupling and Extended Balloon model  
     M - Neural mass model structure (M.input - neuronal drive functions)  
     U - Inputs  
     
    Outputs:  
    -------------------------------------------------------------------------  
     y - BOLD predictions  
     
    This code scales neuronal drive signals by neurovascular coupling parameters  
    and uses it as a single input (per each region) to a haemodynamic function.  
    The outputs of the code are BOLD responses.  
   __________________________________________________________________________  
    Jafarian, A., Litvak, V., Cagnan, H., Friston, K.J. and Zeidman, P., 2019.  
    Neurovascular coupling: insights from multi-modal dynamic causal modelling  
    of fMRI and MEG. arXiv preprint arXiv:1903.07478.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/NVC/spm_nvc_gen.m)
  """

  return _Runtime.call("spm_nvc_gen", *args, **kwargs)
