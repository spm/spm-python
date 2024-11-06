from spm.__wrapper__ import Runtime


def fiff_find_evoked(*args, **kwargs):
    """
       
        [data_sets] = fiff_find_evoked(fname)  
         
        Find all evoked data sets in a fif file and create a list of descriptors  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/fiff_find_evoked.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fiff_find_evoked", *args, **kwargs)
