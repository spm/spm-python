from spm.__wrapper__ import Runtime


def spm_dcm_symm(*args, **kwargs):
  """  Lock ECD orientations by introducing prior correlations  
    FORMAT [pC] = spm_dcm_symm(pV,pE)  
   __________________________________________________________________________  
     
    pE   - prior expectation  
    pV   - prior variance  
    pC   - prior covariance  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_dcm_symm.m)
  """

  return Runtime.call("spm_dcm_symm", *args, **kwargs)
