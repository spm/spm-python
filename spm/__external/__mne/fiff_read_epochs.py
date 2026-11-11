from spm._runtime import Runtime


def fiff_read_epochs(*args, **kwargs):
    r"""
       
        [epochs] = fiff_read_epochs(fname,setno)  
         
        Read epochs from file  
         
         
          Author : Martin Luessi, MGH Martinos Center  
          License : BSD 3-clause  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/fiff_read_epochs.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_read_epochs", *args, **kwargs)
