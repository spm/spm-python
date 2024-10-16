from spm.__wrapper__ import Runtime


def spm_ssm2ccf(*args, **kwargs):
  """  computes cross covariance from state space representation  
    FORMAT [ccf,pst] = spm_ssm2ccf(dfdx,dfdu,dgdx,Hz)  
     
    dfdx - Jacobian  
    dfdu - input matrix  [default: 1]  
    dgdx - output matrix [default: 1]  
    Hz   - frequencies  
     
    ccf  - cross covariance functions  
    pst  - vector of lags for evaluation (seconds)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/spectral/spm_ssm2ccf.m)
  """

  return Runtime.call("spm_ssm2ccf", *args, **kwargs)
