from spm.__wrap__ import _Runtime


def spm_dartel_norm(*args, **kwargs):
  """  Warp individuals to match template  
    FORMAT spm_dartel_norm(job)  
    job.flowfields - Flow-fields  
    job.images     - Image to warp  
    job.interp     - Interpolation method  
    job.K          - 2^K timesteps are used  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DARTEL/spm_dartel_norm.m)
  """

  return _Runtime.call("spm_dartel_norm", *args, **kwargs)
