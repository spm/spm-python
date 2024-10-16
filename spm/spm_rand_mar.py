from spm.__wrapper__ import Runtime


def spm_rand_mar(*args, **kwargs):
  """  Generate random variates from an autoregressive process  
    FORMAT [y] = spm_rand_mar(m,n,a)  
    m   - time bins  
    n   - variates  
    a   - autoregression coefficients  
     
    see also: spm_rand_power_law  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_rand_mar.m)
  """

  return Runtime.call("spm_rand_mar", *args, **kwargs)
