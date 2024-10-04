from spm.__wrap__ import _Runtime


def spm_dcm_fnirs_viewer_result(*args, **kwargs):
  """  GUI for displaying DCM-fNIRS results  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/dcm_fnirs/spm_dcm_fnirs_viewer_result.m)
  """

  return _Runtime.call("spm_dcm_fnirs_viewer_result", *args, **kwargs)
