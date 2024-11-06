from spm.__wrapper__ import Runtime


def mne_read_events(*args, **kwargs):
    """
       
        [eventlist] = mne_read_events(filename)  
         
        Read an event list from a fif file  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/mne_read_events.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mne_read_events", *args, **kwargs)
