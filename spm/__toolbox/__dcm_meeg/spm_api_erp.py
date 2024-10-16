from spm.__wrapper__ import Runtime


def spm_api_erp(*args, **kwargs):
  """  SPM_API_ERP Application M-file for spm_api_erp.fig  
       FIG = SPM_API_ERP launch spm_api_erp GUI.  
       SPM_API_ERP('callback_name', ...) invoke the named callback.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_api_erp.m)
  """

  return Runtime.call("spm_api_erp", *args, **kwargs)
