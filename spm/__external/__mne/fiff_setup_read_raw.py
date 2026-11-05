from spm._runtime import Runtime


def fiff_setup_read_raw(*args, **kwargs):
    r"""
       
        [data] = fiff_setup_read_raw(fname,allow_maxshield)  
         
        Read information about raw data file  
         
        fname               Name of the file to read  
        allow_maxshield     Accept unprocessed MaxShield data  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/fiff_setup_read_raw.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_setup_read_raw", *args, **kwargs)
