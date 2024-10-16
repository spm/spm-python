from spm.__wrapper__ import Runtime


def spm_ndgrid(*args, **kwargs):
  """  Return a matrix of grid points in the domain specified by x  
    FORMAT [X,x] = spm_ndgrid(x)  
     
    x{i):   cell array of vectors specifying support or;  
    x(i):   vector of bin numbers in the range [-1 1]  
     
    x{i):   cell array of vectors specifying support or;  
    X:      (n x m) coordinates of n points in m-D space  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_ndgrid.m)
  """

  return Runtime.call("spm_ndgrid", *args, **kwargs)
