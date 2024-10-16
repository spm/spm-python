from spm.__wrapper__ import Runtime


def spm_dcm_local_minima(*args, **kwargs):
  """  Evaluate the free energy landscape around the posterior  
    FORMAT spm_dcm_local_minima(DCM)  
    DCM - (invert) model structure  
     
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_dcm_local_minima.m)
  """

  return Runtime.call("spm_dcm_local_minima", *args, **kwargs, nargout=0)
