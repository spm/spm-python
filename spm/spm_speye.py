from spm.__wrap__ import _Runtime


def spm_speye(*args, **kwargs):
  """  Sparse leading diagonal matrix  
    FORMAT [D] = spm_speye(m,n,k,c)  
     
    returns an m x n matrix with ones along the k-th leading diagonal. If  
    called with an optional fourth argument c = 1, a wraparound sparse matrix  
    is returned. If c = 2, then empty rows or columns are filled in on the  
    leading diagonal.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_speye.m)
  """

  return _Runtime.call("spm_speye", *args, **kwargs)
