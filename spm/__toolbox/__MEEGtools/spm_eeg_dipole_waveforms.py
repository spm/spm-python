from spm.__wrapper__ import Runtime


def spm_eeg_dipole_waveforms(*args, **kwargs):
    """
      Function for extracting source data using dipoles.  
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/MEEGtools/spm_eeg_dipole_waveforms.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_dipole_waveforms", *args, **kwargs)
