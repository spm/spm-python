from spm.__wrap__ import _Runtime


def spm_ssm2mtf(*args, **kwargs):
  """  computes cross spectral density from state space representation  
    FORMAT [mtf,Hz] = spm_ssm2mtf(dfdx,dfdu,dgdx,Hz)  
     
    dfdx - Jacobian  
    dfdu - input matrix  [default: 1]  
    dgdx - output matrix [default: 1]  
    Hz   - frequencies   [default: based on maximum eigenvalue]  
     
    mtf  - directed or modulation transfer function  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/spectral/spm_ssm2mtf.m)
  """

  return _Runtime.call("spm_ssm2mtf", *args, **kwargs)
