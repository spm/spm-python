from spm.__wrapper__ import Runtime


def fiff_read_evoked_all(*args, **kwargs):
    """
       
        [data] = fiff_read_evoked_all(fname)  
         
        Read all evoked data set (averages only)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/fiff_read_evoked_all.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fiff_read_evoked_all", *args, **kwargs)
