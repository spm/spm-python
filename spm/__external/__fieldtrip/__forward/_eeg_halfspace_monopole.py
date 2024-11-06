from spm.__wrapper__ import Runtime


def _eeg_halfspace_monopole(*args, **kwargs):
    """
      EEG_HALFSPACE_MONOPOLE calculate the leadfield on positions elc for a monopole at  
        position monpos. The halfspace solution requires a plane dividing a conductive zone  
        (cond > 0), from a non-coductive zone (cond = 0).  
         
        Use as  
          [lf] = eeg_halfspace_monopole(monpos, elc, vol)  
         
        See also EEG_INFINITE_DIPOLE, EEG_INFINITE_MONOPOLE, EEG_HALFSPACE_DIPOLE  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/forward/private/eeg_halfspace_monopole.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("eeg_halfspace_monopole", *args, **kwargs)
