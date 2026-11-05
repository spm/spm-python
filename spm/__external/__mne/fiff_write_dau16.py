from spm._runtime import Runtime


def fiff_write_dau16(*args, **kwargs):
    r"""
       
        fiff_write_dau16(fid, kind, data)  
         
        Writes a 16-bit integer tag to a fif file  
         
            fid           An open fif file descriptor  
            kind          Tag kind  
            data          The integers to use as data  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/fiff_write_dau16.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_write_dau16", *args, **kwargs, nargout=0)
