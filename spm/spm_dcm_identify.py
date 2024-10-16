from spm.__wrapper__ import Runtime


def spm_dcm_identify(*args, **kwargs):
  """  Identify the type of DCM. Return an empty string if unknown  
     
    DCM   - the model to evaluate  
     
    model - a string identifying the modality  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_dcm_identify.m)
  """

  return Runtime.call("spm_dcm_identify", *args, **kwargs)
