from spm._runtime import Runtime


def fiff_read_events(*args, **kwargs):
    r"""
       
        [events, mappings] = fiff_read_events(source, tree)  
         
        Read the events  
         
        If tree is specified, source is assumed to be an open file id,  
        otherwise a the name of the file to read. If tree is missing, the  
        meas output argument should not be specified.  
         
         
          Author : Martin Luessi, MGH Martinos Center  
          License : BSD 3-clause  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/fiff_read_events.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_read_events", *args, **kwargs)
