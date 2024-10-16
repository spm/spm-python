from spm.__wrapper__ import Runtime


def spm_dcm_fmri_image(*args, **kwargs):
  """  Image display of A, B, C and D coupling matrices  
    FORMAT spm_dcm_fmri_image(P)  
     
    P.A, P.B{1}, ...     - connections of weighted directed graph  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_dcm_fmri_image.m)
  """

  return Runtime.call("spm_dcm_fmri_image", *args, **kwargs, nargout=0)
