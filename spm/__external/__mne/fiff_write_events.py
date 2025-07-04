from spm._runtime import Runtime


def fiff_write_events(*args, **kwargs):
    """
       
        fiff_write_events(filename,eventlist,mappings)  
         
        Write an event list into a fif file, and include an optional description  
        of the event ids. This function has been adjusted by Jan Mathijs Schoffelen  
        from mne_write_events, with the intention to make a writing function that  
        is symmetric in its behavior w.r.t. fiff_read_events (which can read the  
        mappings). The filename argument can be a string, or a file identifier to  
        an open (for writing) fif-file.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/fiff_write_events.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_write_events", *args, **kwargs, nargout=0)
