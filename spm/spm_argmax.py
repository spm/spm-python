from spm.__wrapper__ import Runtime


def spm_argmax(*args, **kwargs):
  """  Function minimisation using Gauss-Newton  
    FORMAT [P,f] = spm_argmax('fun',varargin,i)  
     
    fun      - inline function f - fun(P,varargin)  
    varargin - function arguments  
    i        - argument to minimise: varargin{i}  
     
    P   - optimised argument  
    f   - optimised value of fun(P)  
     
   --------------------------------------------------------------------------  
    spm_argmax uses numerical derivatives and a and adaptive Gauss-Newton   
    scheme: see also spm_argmin.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_argmax.m)
  """

  return Runtime.call("spm_argmax", *args, **kwargs)
