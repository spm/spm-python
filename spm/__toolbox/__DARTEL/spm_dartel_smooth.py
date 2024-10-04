from spm.__wrap__ import _Runtime


def spm_dartel_smooth(*args, **kwargs):
  """  Smooth tissue probability maps  
    FORMAT [sig,a_new] = spm_dartel_smooth(t,lam,its,vx,a_old)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DARTEL/spm_dartel_smooth.m)
  """

  return _Runtime.call("spm_dartel_smooth", *args, **kwargs)
