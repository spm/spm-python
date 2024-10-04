from spm.__wrap__ import _Runtime


def spm_dcm_contrasts(*args, **kwargs):
  """  Make contrast vector for a DCM  
    FORMAT con = spm_dcm_contrasts(DCM,D)  
     
    DCM    - DCM structure or its filename  
    D      - 'A','B' or 'C' i.e. connectivity matrix of interest  
     
    con    - column vector specifying contrast weights  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_dcm_contrasts.m)
  """

  return _Runtime.call("spm_dcm_contrasts", *args, **kwargs)
