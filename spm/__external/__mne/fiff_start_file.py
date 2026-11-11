from spm._runtime import Runtime


def fiff_start_file(*args, **kwargs):
    r"""
       
        [fid] = fiff_start_file(name)  
          
        Opens a fif file for writing and writes the compulsory header tags  
         
            name           The name of the file to open. It is recommended  
                           that the name ends with .fif  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/fiff_start_file.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_start_file", *args, **kwargs)
