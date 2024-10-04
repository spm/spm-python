from spm.__wrap__ import _Runtime


def spm_ecat2nifti(*args, **kwargs):
  """  Import ECAT 7 images from CTI PET scanners  
    FORMAT N = spm_ecat2nifti(fname,opts)  
    fname    - name of ECAT file  
    opts     - options structure  
     
    N        - NIfTI object (written in current directory)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_ecat2nifti.m)
  """

  return _Runtime.call("spm_ecat2nifti", *args, **kwargs)
