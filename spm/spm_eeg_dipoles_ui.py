from spm.__wrap__ import _Runtime


def spm_eeg_dipoles_ui(*args, **kwargs):
  """  Get dipole locations and orientations from the user  
    FORMAT dipoles = spm_eeg_dipoles_ui  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_eeg_dipoles_ui.m)
  """

  return _Runtime.call("spm_eeg_dipoles_ui", *args, **kwargs)
