from spm._runtime import Runtime


def mne_write_events(*args, **kwargs):
    r"""
       
        mne_write_events(filename,eventlist)  
         
        Write an event list into a fif file  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/mne_write_events.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mne_write_events", *args, **kwargs, nargout=0)
