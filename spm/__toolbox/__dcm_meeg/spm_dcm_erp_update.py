from spm.__wrapper__ import Runtime


def spm_dcm_erp_update(*args, **kwargs):
  """  Set priors over DCM model parameters for Bayesian updating  
    FORMAT DCM = spm_dcm_erp_update(DCM,oldDCM,fields)  
     
    DCM    - DCM structure to be updated  
    oldDCM - inverted DCM with posterior moments  
    fields - character array of fields to be updated: e.g.,{'A','B'}  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_dcm_erp_update.m)
  """

  return Runtime.call("spm_dcm_erp_update", *args, **kwargs)
