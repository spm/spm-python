from spm.__wrapper__ import Runtime


def _eeg_halfspace_dipole(*args, **kwargs):
    """
      EEG_HALFSPACE_DIPOLE calculate the leadfield on electrode positions elc  
        for a dipole at position dippos. The halfspace solution requires a plane dividing a  
        conductive zone (cond > 0), from a non-coductive zone (cond = 0).  
         
        Use as  
          [lf] = eeg_halfspace_dipole(dippos, elc, vol)  
         
        See also EEG_INFINITE_DIPOLE, EEG_INFINITE_MONOPOLE, EEG_HALFSPACE_MONOPOLE  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/forward/private/eeg_halfspace_dipole.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("eeg_halfspace_dipole", *args, **kwargs)
