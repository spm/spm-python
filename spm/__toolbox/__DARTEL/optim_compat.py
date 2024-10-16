from spm.__wrapper__ import Runtime


def optim_compat(*args, **kwargs):
  """  Compatibility function for optimN and optimNn  
    FORMAT varargout = optim_compat(bc,varargin)  
    bc - boundary condition (0=circulant, 1-Neumann)  
     
    Call the new spm_field function via the old API of the optimN and  
    optimNn functions.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DARTEL/optim_compat.m)
  """

  return Runtime.call("optim_compat", *args, **kwargs)
