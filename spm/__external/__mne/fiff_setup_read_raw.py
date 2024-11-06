from spm.__wrapper__ import Runtime


def fiff_setup_read_raw(*args, **kwargs):
    """
       
        [data] = fiff_setup_read_raw(fname,allow_maxshield)  
         
        Read information about raw data file  
         
        fname               Name of the file to read  
        allow_maxshield     Accept unprocessed MaxShield data  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/fiff_setup_read_raw.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fiff_setup_read_raw", *args, **kwargs)
