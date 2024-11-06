from spm.__wrapper__ import Runtime


def _eeg_infinite_dipole(*args, **kwargs):
    """
      EEG_INFINITE_DIPOLE calculate the infinite medium leadfield on electrode positions  
        elc for a dipole at dippos and with the conductivity cond.  
         
        Use as  
          [lf] = eeg_infinite_dipole(R, elc, vol)  
         
        See also EEG_INFINITE_MONOPOLE, EEG_HALFSPACE_DIPOLE, EEG_HALFSPACE_MONOPOLE  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/forward/private/eeg_infinite_dipole.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("eeg_infinite_dipole", *args, **kwargs)
