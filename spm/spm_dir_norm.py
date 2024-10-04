from spm.__wrap__ import _Runtime


def spm_dir_norm(*args, **kwargs):
  """  Normalisation of a (Dirichlet) conditional probability matrix  
    FORMAT A = spm_dir_norm(a)  
     
    a    - (Dirichlet) parameters of a conditional probability matrix  
     
    A    - conditional probability matrix  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_dir_norm.m)
  """

  return _Runtime.call("spm_dir_norm", *args, **kwargs)
