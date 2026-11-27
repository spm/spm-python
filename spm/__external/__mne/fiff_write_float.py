from spm._runtime import Runtime


def fiff_write_float(*args, **kwargs):
    r"""
       
        fiff_write_float(fid,kind,data)  
          
        Writes a single-precision floating point tag to a fif file  
         
            fid           An open fif file descriptor  
            kind          Tag kind  
            data          The data  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/fiff_write_float.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_write_float", *args, **kwargs, nargout=0)
