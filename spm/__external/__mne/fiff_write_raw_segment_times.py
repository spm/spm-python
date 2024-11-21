from spm.__wrapper__ import Runtime


def fiff_write_raw_segment_times(*args, **kwargs):
    """
        FIFF_WRITE_RAW_SEGMENT_TIMES   Write chunck of raw data to disk  
              [] = FIFF_WRITE_RAW_SEGMENT_TIMES(FNAME, RAW, FROM, TO, SEL)  
         
          The functions reads data from a file specified by raw  
          which is obtained with fiff_setup_read_raw  
         
        fname              - the name of the file where to write  
        raw                - structure returned by fiff_setup_read_raw  
        from               - starting time of the segment in seconds  
        to                 - end time of the segment in seconds  
        sel                - optional channel selection vector  
        drop_small_buffer  - optional bool to say if the last data buffer is dropped  
                             to make sure all buffers have the same size  
                             (required by maxfilter)  
        buffer_size_sec    - float (size of data buffers in seconds)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/fiff_write_raw_segment_times.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fiff_write_raw_segment_times", *args, **kwargs, nargout=0)
