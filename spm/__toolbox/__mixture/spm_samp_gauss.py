from spm.__wrap__ import _Runtime


def spm_samp_gauss(*args, **kwargs):
  """  Sample from a Gaussian PDF  
    FORMAT [x] = spm_samp_gauss (m, C, N, dC, vC)  
    m     [d x 1] mean  
    C     [d x d] covar  
    N     Number of samples  
    dC    diagonalised C [d x 1]  
    vC    eigenvectors of C [d x d]  
     
    x     [N x d] matrix of samples  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mixture/spm_samp_gauss.m)
  """

  return _Runtime.call("spm_samp_gauss", *args, **kwargs)
