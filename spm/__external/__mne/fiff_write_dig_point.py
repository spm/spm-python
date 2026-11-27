from spm._runtime import Runtime


def fiff_write_dig_point(*args, **kwargs):
    r"""
       
        fiff_write_dig_point(fid,dig)  
          
        Writes a digitizer data point into a fif file  
         
            fid           An open fif file descriptor  
            dig           The point to write  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/fiff_write_dig_point.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_write_dig_point", *args, **kwargs, nargout=0)
