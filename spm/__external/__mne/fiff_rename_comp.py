from spm.__wrapper__ import Runtime


def fiff_rename_comp(*args, **kwargs):
    """
    fiff_rename_comp is a function.  
          comp = fiff_rename_comp(comp, ch_rename)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/fiff_rename_comp.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fiff_rename_comp", *args, **kwargs)
