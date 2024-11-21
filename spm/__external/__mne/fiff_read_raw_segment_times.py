from spm.__wrapper__ import Runtime


def fiff_read_raw_segment_times(*args, **kwargs):
    """
       
        [data,times] = fiff_read_raw_segment_times(raw,from,to)  
         
        Read a specific raw data segment  
         
        raw    - structure returned by fiff_setup_read_raw  
        from   - starting time of the segment in seconds  
        to     - end time of the segment in seconds  
        sel    - optional channel selection vector  
         
        data   - returns the data matrix (channels x samples)  
        times  - returns the time values corresponding to the samples (optional)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/fiff_read_raw_segment_times.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fiff_read_raw_segment_times", *args, **kwargs)
