from spm.__wrapper__ import Runtime


def spm_vecfun(*args, **kwargs):
  """  Apply a function to the numeric elements of a cell or structure array  
    FORMAT [X] = spm_vecfun(X,fun)  
    X   - numeric, cell or stucture array  
    fun - function handle  
   __________________________________________________________________________  
     
    e.g., pE = spm_vecfun(pE,@log)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_vecfun.m)
  """

  return Runtime.call("spm_vecfun", *args, **kwargs)
