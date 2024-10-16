from spm.__wrapper__ import Runtime


def spm_eeg_dipoles_ui(*args, **kwargs):
  """  Get dipole locations and orientations from the user  
    FORMAT dipoles = spm_eeg_dipoles_ui  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_eeg_dipoles_ui.m)
  """

  return Runtime.call("spm_eeg_dipoles_ui", *args, **kwargs)
