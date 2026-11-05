from spm._runtime import Runtime


def fiff_find_evoked(*args, **kwargs):
    r"""
       
        [data_sets] = fiff_find_evoked(fname)  
         
        Find all evoked data sets in a fif file and create a list of descriptors  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/fiff_find_evoked.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_find_evoked", *args, **kwargs)
