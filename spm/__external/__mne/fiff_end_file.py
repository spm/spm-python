from spm._runtime import Runtime


def fiff_end_file(*args, **kwargs):
    r"""
       
        fiff_end_file(fid)  
         
        Writes the closing tags to a fif file and closes the file  
         
            fid           An open fif file descriptor  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/fiff_end_file.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_end_file", *args, **kwargs, nargout=0)
