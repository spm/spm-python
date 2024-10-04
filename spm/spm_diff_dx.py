from spm.__wrap__ import _Runtime


def spm_diff_dx(*args, **kwargs):
  """  Optimisation of finite difference for numerical differentiation  
    FORMAT [dx] = spm_diff_dx(f,x,...,n)  
    FORMAT [dx] = spm_diff_dx(f,x,...,n,V)  
    FORMAT [dx] = spm_diff_dx(f,x,...,n,'q')  
     
    f      - [inline] function f(x{1},...)  
    x      - input argument[s]  
    n      - arguments to differentiate w.r.t.  
     
    dx     - 'best' step size  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_diff_dx.m)
  """

  return _Runtime.call("spm_diff_dx", *args, **kwargs)
