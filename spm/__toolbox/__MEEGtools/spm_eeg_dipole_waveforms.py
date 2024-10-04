from spm.__wrap__ import _Runtime


def spm_eeg_dipole_waveforms(*args, **kwargs):
  """  Function for extracting source data using dipoles.  
    FORMAT sD = spm_eeg_dipole_waveforms(S)  
     
    S                    - input structure (optional)  
    (optional) fields of S:  
      S.D                - MEEG object or filename of M/EEG mat-file  
      S.dipoles          - (optional)  
        Structure describing the dipoles  
        dipoles.pnt      - Nx3 matrix of locations in MNI coordinates  
        dipoles.ori      - Nx3 matrix of orientations in MNI coordinates  
        dipoles.label    - Nx1 cell array of dipole labels  
     
    Output:  
    sD                   - MEEG object (also written on disk)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/MEEGtools/spm_eeg_dipole_waveforms.m)
  """

  return _Runtime.call("spm_eeg_dipole_waveforms", *args, **kwargs)
