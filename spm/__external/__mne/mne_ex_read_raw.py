from spm.__wrapper__ import Runtime


def mne_ex_read_raw(*args, **kwargs):
    """
       
          Example of reading raw data  
         
          [ data, times ] = mne_ex_read_raw(fname,from,to,in_samples,dest_comp);  
         
          data        - The data read, compensated and projected, channel by  
                        channel  
          times       - The time points of the samples, in seconds  
         
         
          fname       - The name of the input file  
          from        - Starting time or sample  
          to          - Ending time or sample  
          in_samples  - Are from and to given in samples rather than in seconds  
                        (optional)  
          dest_comp   - Desired (CTF) compensation in the output data (optional)  
         
          NOTE: The purpose of this function is to demonstrate the raw data reading  
          routines. In real world, you probably make multiple calls to  
          fiff_read_raw_segment_times or fiff_read_raw_segment  
          between open and close  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/mne_ex_read_raw.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mne_ex_read_raw", *args, **kwargs)
