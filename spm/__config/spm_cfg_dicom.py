from spm.__wrap__ import _Runtime


def spm_cfg_dicom(*args, **kwargs):
  """  SPM Configuration file for DICOM Import  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_dicom.m)
  """

  return _Runtime.call("spm_cfg_dicom", *args, **kwargs)
