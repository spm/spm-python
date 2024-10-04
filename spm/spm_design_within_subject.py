from spm.__wrap__ import _Runtime


def spm_design_within_subject(*args, **kwargs):
  """  Set up within-subject design when specified subject by subject  
    FORMAT [I,P,cov] = spm_design_within_subject(fblock,cov)  
     
    fblock   - Part of job structure containing within-subject design info  
    cov      - Part of job structure containing covariate info  
     
    I        - Nscan x 4 factor matrix  
    P        - List of scans  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_design_within_subject.m)
  """

  return _Runtime.call("spm_design_within_subject", *args, **kwargs)
