from spm.__wrap__ import _Runtime


def spm_vol_nifti(*args, **kwargs):
  """  Get header information for a NIFTI-1 image  
    FORMAT V = spm_vol_nifti(P,n)  
    P   - filename or NIfTI object  
    n   - volume id (a 1x2 array, e.g. [3,1])  
     
    V   - a structure containing the image volume information  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_vol_nifti.m)
  """

  return _Runtime.call("spm_vol_nifti", *args, **kwargs)
