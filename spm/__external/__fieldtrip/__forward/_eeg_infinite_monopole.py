from spm.__wrapper__ import Runtime


def _eeg_infinite_monopole(*args, **kwargs):
    """
      EEG_INFINITE_MONOPOLE calculate the infinite medium potential for a monopole  
         
        Use as  
          [lf] = eeg_infinite_monopole(monpos, elc, vol)  
         
        Implemented from Malmivuo J, Plonsey R, Bioelectromagnetism (1993)  
        http://www.bem.fi/book/08/08.htm  
         
        See also EEG_INFINITE_DIPOLE, EEG_HALFSPACE_DIPOLE, EEG_HALFSPACE_MONOPOLE  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/forward/private/eeg_infinite_monopole.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("eeg_infinite_monopole", *args, **kwargs)
