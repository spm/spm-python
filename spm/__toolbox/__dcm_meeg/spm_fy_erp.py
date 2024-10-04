from spm.__wrap__ import _Runtime


def spm_fy_erp(*args, **kwargs):
  """  Feature selection for erp models   
    FORMAT f = spm_fy_erp(y,M)  
    f = y*M.U;  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_fy_erp.m)
  """

  return _Runtime.call("spm_fy_erp", *args, **kwargs)
