from spm.__wrapper__ import Runtime


def spm_vb_taylor_R(*args, **kwargs):
  """  Get Taylor series approximation to posterior correlation matrices  
    FORMAT [slice] = spm_vb_taylor_R(Y,slice)  
     
    Y        - data  
    slice    - VB-GLMAR data structure  
     
    See paper VB3.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_vb_taylor_R.m)
  """

  return Runtime.call("spm_vb_taylor_R", *args, **kwargs)
