from spm._runtime import Runtime


def fiff_read_raw_segment_times(*args, **kwargs):
    r"""
       
        [data,times] = fiff_read_raw_segment_times(raw,from,to)  
         
        Read a specific raw data segment  
         
        raw    - structure returned by fiff_setup_read_raw  
        from   - starting time of the segment in seconds  
        to     - end time of the segment in seconds  
        sel    - optional channel selection vector  
         
        data   - returns the data matrix (channels x samples)  
        times  - returns the time values corresponding to the samples (optional)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/fiff_read_raw_segment_times.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_read_raw_segment_times", *args, **kwargs)
