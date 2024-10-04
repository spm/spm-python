from spm.__wrap__ import _Runtime


def spm_mtx_cos(*args, **kwargs):
  """  returns the cosine of the angle between A and B  
    FORMAT c = spm_mtx_cos(A,B)  
     
    a    - (Dirichlet) parameters of a conditional probability matrix  
     
    c = arccos( <A|B> /(<A|A><B|B>))  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_mtx_cos.m)
  """

  return _Runtime.call("spm_mtx_cos", *args, **kwargs)
