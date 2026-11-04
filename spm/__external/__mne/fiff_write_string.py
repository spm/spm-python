from spm._runtime import Runtime


def fiff_write_string(*args, **kwargs):
    r"""
       
        fiff_write_string(fid,kind,data)  
          
        Writes a string tag  
         
            fid           An open fif file descriptor  
            kind          The tag kind  
            data          The string data to write  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/fiff_write_string.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_write_string", *args, **kwargs, nargout=0)
