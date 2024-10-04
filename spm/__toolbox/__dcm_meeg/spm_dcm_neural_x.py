from spm.__wrap__ import _Runtime


def spm_dcm_neural_x(*args, **kwargs):
  """  Return the fixed point or steady-state of a neural mass DCM  
    FORMAT [x] = spm_dcm_neural_x(P,M)  
     
    P   - parameter structure  
    M   - model structure  
     
    x   - steady state solution  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_dcm_neural_x.m)
  """

  return _Runtime.call("spm_dcm_neural_x", *args, **kwargs)
