from spm.__wrapper__ import Runtime


def fiff_write_raw_segment(*args, **kwargs):
    """
        FIFF_WRITE_RAW_SEGMENT   Write chunck of raw data to disk  
              [] = FIFF_WRITE_RAW_SEGMENT(FNAME, RAW, FROM, TO, SEL)  
         
          The functions reads data from a file specified by raw  
          which is obtained with fiff_setup_read_raw  
         
        fname                - the name of the file where to write  
        raw                  - structure returned by fiff_setup_read_raw  
        from                 - first sample to include. If omitted, defaults to the  
                               first sample in data  
        to                   - last sample to include. If omitted, defaults to the last  
                               sample in data  
        sel                  - optional channel selection vector  
        drop_small_buffer    - optional bool to say if the last data buffer is dropped  
                               to make sure all buffers have the same size  
                               (required by maxfilter)  
        buffer_size          - float (size of data buffers)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/fiff_write_raw_segment.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fiff_write_raw_segment", *args, **kwargs, nargout=0)
