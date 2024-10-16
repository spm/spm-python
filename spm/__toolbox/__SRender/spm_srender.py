from spm.__wrapper__ import Runtime


def spm_srender(*args, **kwargs):
  """  A function for rendering surfaces  
    FORMAT spm_srender(job)  
    job - a job structure (see tbx_cfg_render.m)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/SRender/spm_srender.m)
  """

  return Runtime.call("spm_srender", *args, **kwargs, nargout=0)
