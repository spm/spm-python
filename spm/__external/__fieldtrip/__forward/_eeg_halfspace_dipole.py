from spm._runtime import Runtime


def _eeg_halfspace_dipole(*args, **kwargs):
    r"""
      EEG_HALFSPACE_DIPOLE calculate the leadfield on electrode positions elc  
        for a dipole at position dippos. The halfspace solution requires a plane dividing a  
        conductive zone (cond > 0), from a non-coductive zone (cond = 0).  
         
        Use as  
          [lf] = eeg_halfspace_dipole(dippos, elc, vol)  
         
        See also EEG_INFINITE_DIPOLE, EEG_INFINITE_MONOPOLE, EEG_HALFSPACE_MONOPOLE  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/forward/private/eeg_halfspace_dipole.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("eeg_halfspace_dipole", *args, **kwargs)
