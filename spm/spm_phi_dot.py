from spm.__wrapper__ import Runtime


def spm_phi_dot(*args, **kwargs):
  """  Return the derivative of the logistic function  
    FORMAT [y] = spm_phi_dot(x)  
    see spm_phi and spm_inv_phi  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_phi_dot.m)
  """

  return Runtime.call("spm_phi_dot", *args, **kwargs)
