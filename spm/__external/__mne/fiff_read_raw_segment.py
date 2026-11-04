from spm._runtime import Runtime


def fiff_read_raw_segment(*args, **kwargs):
    r"""
       
        [data,times] = fiff_read_raw_segment(raw,from,to,sel)  
         
        Read a specific raw data segment  
         
        raw    - structure returned by fiff_setup_read_raw  
        from   - first sample to include. If omitted, defaults to the  
                 first sample in data  
        to     - last sample to include. If omitted, defaults to the last  
                 sample in data  
        sel    - optional channel selection vector  
         
        data   - returns the data matrix (channels x samples)  
        times  - returns the time values corresponding to the samples (optional)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/fiff_read_raw_segment.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_read_raw_segment", *args, **kwargs)
