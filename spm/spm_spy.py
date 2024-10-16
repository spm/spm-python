from spm.__wrapper__ import Runtime


def spm_spy(*args, **kwargs):
  """  Pretty version of spy  
    FORMAT spm_spy(X,Markersize,m)  
    X    - sparse {m x n} matrix  
     
    See also: spy  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_spy.m)
  """

  return Runtime.call("spm_spy", *args, **kwargs, nargout=0)
