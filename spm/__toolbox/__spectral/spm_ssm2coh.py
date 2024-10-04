from spm.__wrap__ import _Runtime


def spm_ssm2coh(*args, **kwargs):
  """  computes coherence from state space representation  
    FORMAT [coh,fsd] = spm_ssm2coh(dfdx,dfdu,dgdx,Hz)  
     
    dfdx - Jacobian  
    dfdu - input matrix  [default: 1]  
    dgdx - output matrix [default: 1]  
    Hz   - frequencies   [default: based on maximum eigenvalue]  
     
    coh            - coherence  
    fsd            - frequency specific delay (seconds)   
                   - phase-delay/radial frequency  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/spectral/spm_ssm2coh.m)
  """

  return _Runtime.call("spm_ssm2coh", *args, **kwargs)
