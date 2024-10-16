from spm.__wrapper__ import Runtime


def spm_svd(*args, **kwargs):
  """  Computationally efficient SVD (that can handle sparse arguments)  
    FORMAT [U,S,V] = spm_svd(X,u)  
    X    - (m x n) matrix  
    u    - threshold (1 > u > 0) for normalized eigenvalues (default = 1e-6)  
         - a value of zero induces u = 64*eps  
     
    U    - {m x p} singular vectors  
    V    - {m x p} singular variates  
    S    - {p x p} singular values  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_svd.m)
  """

  return Runtime.call("spm_svd", *args, **kwargs)
