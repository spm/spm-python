from spm.__wrap__ import _Runtime


def spm_logdet(*args, **kwargs):
  """  Compute the log of the determinant of positive (semi-)definite matrix C  
    FORMAT H = spm_logdet(C)  
    H = log(det(C))  
     
    spm_logdet is a computationally efficient operator that can deal with  
    full or sparse matrices. For non-positive definite cases, the determinant  
    is considered to be the product of the positive singular values.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_logdet.m)
  """

  return _Runtime.call("spm_logdet", *args, **kwargs)
