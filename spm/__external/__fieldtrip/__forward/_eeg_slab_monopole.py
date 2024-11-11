from spm.__wrapper__ import Runtime


def _eeg_slab_monopole(*args, **kwargs):
    """
      EEG_SLAB_MONOPOLE calculate the strip medium leadfield  
        on positions pnt for a monopole at position rd and conductivity cond  
        The halfspace solution requires a plane dividing a conductive zone of  
        conductivity cond, from a non coductive zone (cond = 0)  
                
        [lf] = eeg_slab_monopole(rd, elc, cond)  
         
        Implemented from Malmivuo J, Plonsey R, Bioelectromagnetism (1993)  
        http://www.bem.fi/book/index.htm  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/forward/private/eeg_slab_monopole.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("eeg_slab_monopole", *args, **kwargs)
