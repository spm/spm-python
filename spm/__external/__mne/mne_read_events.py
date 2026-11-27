from spm._runtime import Runtime


def mne_read_events(*args, **kwargs):
    r"""
       
        [eventlist] = mne_read_events(filename)  
         
        Read an event list from a fif file  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/mne_read_events.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mne_read_events", *args, **kwargs)
