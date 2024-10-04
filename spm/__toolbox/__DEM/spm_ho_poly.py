from spm.__wrap__ import _Runtime


def spm_ho_poly(*args, **kwargs):
  """  General polynomial mapping with derivatives  
    FORMAT Y = spm_ho_poly(P,M,U)  
     
    P    - polynomial parameters (P{i} = i-th order coefficients)  
    M    - model structure  
    U    - (m,n) inputs  
     
    Y(i) =  P{1} + P{2}*U(:,i) + P{3}*kron(U(:,i),U(:,i)) + ...  
     
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/spm_ho_poly.m)
  """

  return _Runtime.call("spm_ho_poly", *args, **kwargs)
