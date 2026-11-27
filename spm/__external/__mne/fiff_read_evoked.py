from spm._runtime import Runtime


def fiff_read_evoked(*args, **kwargs):
    r"""
       
        [data] = fiff_read_evoked(fname,setno)  
         
        Read one evoked data set  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/fiff_read_evoked.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_read_evoked", *args, **kwargs)
